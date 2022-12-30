import pandas
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# defining the filepath
filePath = r'Combined_Flights_2021.csv'
if rank == 0:
    print(f'\nUsing {size} nodes\n')

    def distribute(recordcount: int, n_processes):
        rows2skip = 1
        distribution = [[recordcount - rows2skip, rows2skip]]
        rows2skip = recordcount
        for _ in range(1, n_processes - 1):
            distribution.append([recordcount, rows2skip])
            rows2skip = rows2skip + recordcount
        distribution.append([None, rows2skip])  # type: ignore
        return distribution
    # method to find the record count
    def row_count(filePath):
        with open(filePath) as f:
            rowcount = sum(1 for _ in open(filePath))
        return rowcount
    # fucntion to display the results the query
    def ques(diverted):
        print(f'Diverted Flights Count,20th-30th November 2021= {diverted}')

    executors = size - 1
    tot_rows = row_count(filePath)
    chunkDistribution = distribute(recordcount=(tot_rows // executors)+1, n_processes=executors)

    start = MPI.Wtime()  
    for worker in range(1, size):
        CHUNKS = worker - 1
        comm.send(chunkDistribution[CHUNKS], dest=worker)

    diverted=0
    for worker in (range(1, size)):  # receive
        answer = comm.recv(source=worker)
        diverted += answer

    ques(diverted)

    end = MPI.Wtime()
    total_time = end - start
    print(f'with {size} workers, it took {round(total_time,2)} seconds..')

elif rank > 0:
    # method to filter the data and get the results in a list
    def chunk_ques(df):
        Diverted_Flights = df[
            (df.Diverted == True) & (df['FlightDate'] >= "2021-11-20") & (df['FlightDate'] <= "2021-11-30")]
        return Diverted_Flights["Airline"].count()
        
    CHUNKS = comm.recv()
    columns = list(pandas.read_csv(filePath, skiprows=0, nrows=0).columns)
    df = pandas.read_csv(filePath, nrows=CHUNKS[0], skiprows=CHUNKS[1], names=columns)
    answer = chunk_ques(df)
    comm.send(answer, dest=0)