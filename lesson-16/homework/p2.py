import pandas as pd

df=pd.read_json('iris.json')
print(df.shape)
print(df.columns)