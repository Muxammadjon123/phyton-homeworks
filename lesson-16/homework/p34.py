import pyarrow.dataset as ds
import pandas as pd

dataset = ds.dataset("flights", format="parquet")
table = dataset.to_table()
df = table.to_pandas()

value_missing=df.isna().sum()
print(f'Missing values:\n{value_missing}')

numeric_cols = df.select_dtypes(include='number').columns

for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

print("\nAll numeric columns' missing values filled with column means.")