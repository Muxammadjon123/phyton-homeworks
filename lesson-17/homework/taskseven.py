import pandas as pd

#reading from file
df=pd.read_csv('employee.csv')

def normalize(x):
    return (x - x.min()) / (x.max() - x.min())

#grouping the department
grouped=df.groupby('DEPARTMENT')

#using apply to normalize
final_df=grouped['BASE_SALARY'].apply(normalize)
print(final_df)

