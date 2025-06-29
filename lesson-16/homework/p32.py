import pandas as pd

df=pd.read_excel('titanic.xlsx')

df_age=df['Age']
maximum_age=df_age.max()
minimum_age=df_age.min()
sum_age=df_age.sum()

print(f'Maximum age:{maximum_age}\nMinimum age:{minimum_age}\nSum of passanger age:{sum_age}')