import pandas as pd

df=pd.read_json('iris.json')

numeric_df=df.select_dtypes(include='number')

mean=numeric_df.mean()
median=numeric_df.median()
standard_deviation=numeric_df.std()

print(f'Mean:{mean}\nMedian:{median}\nStandard Deviation"{standard_deviation}')
