import pandas as pd
from mpi4py import MPI
pd.options.mode.chained_assignment=None  # type: ignore

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# defining the filepath
filePath = r'Combined_Flights_2021.csv'

if rank == 0:

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
    def ques(lst):
        formattedL = [i.strftime('%d/%m/%Y') for i in lst]
        print(f'Dates were not recorded/went missing= \n{set(formattedL)}')
        print("total:",len(set(formattedL)))

    executors = size - 1
    tot_rows = row_count(filePath)
    chunk_distribution = distribute(recordcount=(tot_rows // executors)+1, n_processes=executors)  # type: ignore

    start = MPI.Wtime()  # Start Time ------------------------------------------------

    for worker in range(1, size):
        chunks = worker - 1
        comm.send(chunk_distribution[chunks], dest=worker)

    resultlist = []
    for worker in (range(1, size)):  # receive
        Rlist = comm.recv(source=worker)
        resultlist += Rlist

    ques(resultlist)

    end = MPI.Wtime()  # End Time ------------------------------------------------

    total_time = end - start
    print(f'with {size} workers, it took {round(total_time,2)} seconds..')

elif rank > 0:
    # method to filter the data and get the results in a list
    def chunk_ques(df):
        df['FlightDate'] = pd.to_datetime(df['FlightDate'], format='%Y-%m-%d')
        deptime = df[df["DepTime"].isna()]
        deptime['FlightDate'] = deptime['FlightDate'].dt.date
        return deptime["FlightDate"].unique().tolist()

    chunks = comm.recv()
    columns = list(pd.read_csv(filePath, skiprows=0, nrows=0).columns)
    df = pd.read_csv(filePath, nrows=chunks[0], skiprows=chunks[1], names=columns)
    Rlist = chunk_ques(df)
    comm.send(Rlist, dest=0)