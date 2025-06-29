import pandas as pd
from collections import Counter

df=pd.read_excel('titanic.xlsx')

df_older=df[df['Age']>30]

df_gender_counts=df_older['Sex'].value_counts()

print(df_older)
print("Gender counts:\n")
print(df_gender_counts)