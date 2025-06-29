import pandas as pd

#function creation 
def classify(age):
    if pd.isna(age):
        return 'Unknown'
    else:
        return 'Child' if age<18 else 'Adult'
#reading from filter
df=pd.read_excel('titanic.xlsx')

#Age_Group creation
df['Age_Group']=df['Age'].apply(classify)
print(df)
    
