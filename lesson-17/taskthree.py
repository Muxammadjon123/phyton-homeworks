import pandas as pd

#reading from excel file
df=pd.read_excel('titanic.xlsx')
df
#creating grouped data frame
grouped = df.groupby('Pclass').agg({
    'Age': 'mean',           # Average age
    'Fare': 'sum',           # Total fare
    'PassengerId': 'count'   # Count of passengers 
})

#creating a new dat frame columns

grouped.columns=['Average_Age', 'Total_Fare', 'Passenger_Count']
grouped=grouped.reset_index()
print(grouped)

