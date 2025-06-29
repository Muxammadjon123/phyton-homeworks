import pandas as pd
def categorize(series):
    if series['duration']<60:
        return 'Short'
    elif 60<=series['duration']<120:
        return "Medium"
    else:
        return 'Long'
    
#Reading from csv file
df=pd.read_csv('movie.csv')
df['Category']=df.apply(categorize,axis=1)
print(df[['duration','Category']])