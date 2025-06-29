import pandas as pd

df=pd.read_json('iris.json')

df.columns=[col.lower() for col in df.columns]

selected_df=df[['sepallength','sepalwidth']]
print(selected_df)