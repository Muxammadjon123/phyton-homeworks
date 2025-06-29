import pandas as pd

#filtering the survivors
def filter_survivors(df):
    return df[df['Survived']==1]

#filling missing ages
def fill_missing(df):
    df['Age']=df['Age'].fillna(df['Age'].mean())
    return df

#fare per age

def fare_age(df):
    df['Fare_Per_Age'] = df['Fare'] / df['Age']
    return df

#reading from file
df=pd.read_excel('titanic.xlsx')

#using pipe to create pipeline
result = (
    df.pipe(filter_survivors)
      .pipe(fill_missing)
      .pipe(fare_age)
)
print(result)