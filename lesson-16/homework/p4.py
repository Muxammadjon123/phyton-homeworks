import pandas as pd

url = 'data/flights'

df = pd.read_parquet(url)
df.info()
