import pyarrow.dataset as ds
import pandas as pd
dataset = ds.dataset("flights", format="parquet")
table = dataset.to_table()
df = table.to_pandas()

df_columns=df[['origin','dest','carrier']]
print(df_columns.head())

df.unique=df['dest'].nunique()
print("Number of unique destinations")

