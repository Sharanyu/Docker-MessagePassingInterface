import pandas
from collections import Counter
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# defining the filepath
filePath = r'Combined_Flights_2021.csv'
if rank == 0:
    print(f'Using {size} nodes')

    def distribute(records: int, n_processes):
        rows2skip = 1
        distribution = [[records - rows2skip, rows2skip]]
        rows2skip = records

        for _ in range(1, n_processes - 1):
            distribution.append([records, rows2skip])
            rows2skip = rows2skip + records

        distribution.append([None, rows2skip])  # type: ignore
        return distribution

    # fucntion to display the results the query
    def ques(lst):
        print(f'Most canceled flights in September 2021= {Counter(lst).most_common()[0][0]}')

    # method to find the record count
    def row_count(filePath):
        with open(filePath) as f:
            rowcount = sum(1 for _ in open(filePath))
        return rowcount

    executors = size - 1
    totalrecords = row_count(filePath)
    chunk_distribution = distribute(records=(totalrecords // executors) + 1, n_processes=executors)

    start = MPI.Wtime()
    for worker in range(1, size):
        CHUNKS = worker - 1
        comm.send(chunk_distribution[CHUNKS], dest=worker)

    finallist = []

    for worker in (range(1, size)):  # receive
        fetch = comm.recv(source=worker)
        finallist += fetch
    ques(finallist)
    end = MPI.Wtime() 

    total_time = end - start
    print(f'with {size} workers, it took {round(total_time,2)} seconds..')

elif rank > 0:
    # method to filter the data and get the results in a list
    def T3(df_data):
        Canceled_Flights = df_data[
            (df_data.Cancelled == True) & (df_data['FlightDate'] > "2021-08-31") & (df_data['FlightDate'] < "2021-10-01")]
        return Canceled_Flights["Airline"].values.tolist()

    CHUNKS = comm.recv()
    cols = list(pandas.read_csv(filePath, skiprows=0, nrows=0).columns)
    df_data = pandas.read_csv(filePath, nrows=CHUNKS[0], skiprows=CHUNKS[1], names=cols)
    fetch = T3(df_data)
    comm.send(fetch, dest=0)