import pandas as pd

#reading from parquet file
df=pd.read_parquet('flights')
#grouping
grouped=df.groupby(['Year','Month']).agg({
    'ArrDelay': 'mean', #mean
    'DepDelay': 'max', #max
    'Year': 'count' #number of flights
}).rename({ #changing column names
    'Year':'TotalFlights',
    'ArrDelay': 'AvgArrDelay',
    'DepDelay': 'MaxDepDelay'
}).reset_index() #setting indexes as 0,1,2,3

print(grouped)