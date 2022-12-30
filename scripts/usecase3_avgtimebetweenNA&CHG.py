import pandas
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

filePath = r'Combined_Flights_2021.csv'

if rank == 0:
    print(f'\nUsing {size} workers\n')

    def distribute(recordcount: int, n_processes):
        rows2skip = 1
        distribution = [[recordcount - rows2skip, rows2skip]]
        rows2skip = recordcount
        for _ in range(1, n_processes - 1):
            distribution.append([recordcount, rows2skip])
            rows2skip = rows2skip + recordcount
        distribution.append([None, rows2skip])  # type: ignore
        return distribution
    # fucntion to display the results the query
    def ques(avg_time, executors):
        result = f'{(avg_time / executors):.1f}'
        print(f'Average Airtime between Nashville and Chicago : {result} mins')
    # method to find the record count
    def row_count(filePath):
        with open(filePath) as f:
            rowcount = sum(1 for _ in open(filePath))
        return rowcount
    executors = size - 1
    tot_rows = row_count(filePath)
    chunk_distribution = distribute(recordcount=(tot_rows // executors)+1, n_processes=executors)  # type: ignore

    start = MPI.Wtime()
    for worker in range(1, size):
        chunk_to_process = worker - 1
        comm.send(chunk_distribution[chunk_to_process], dest=worker)

    avg_time = 0

    for worker in (range(1, size)):  # receive
        result = comm.recv(source=worker)
        avg_time += result

    ques(avg_time, executors)

    end = MPI.Wtime()

    total_time = end - start
    print(f'with {size} workers, it took {round(total_time,2)} seconds..')


elif rank > 0:
    # method to filter the data and get the results in a list
    def chunk_ques(df):
        df['FlightDate'] = pandas.to_datetime(df['FlightDate'], format='%Y-%m-%d')
        flights = df[(df.OriginCityName =="Nashville, TN") & (df.DestCityName =="Chicago, IL")]
        return flights["AirTime"].mean()

    chunk_to_process = comm.recv()
    columns=list(pandas.read_csv(filePath, skiprows=0, nrows=0).columns)
    df = pandas.read_csv(filePath, nrows=chunk_to_process[0], skiprows=chunk_to_process[1],names=columns)
    result =  chunk_ques(df)
    comm.send(result, dest=0)
