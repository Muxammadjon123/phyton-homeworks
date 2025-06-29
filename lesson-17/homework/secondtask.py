import pandas as pd

#loading data from csv file
df=pd.read_csv('movie.csv')

#creating two smaller data frames
subdf_1=df[['director_name','color']]
subdf_2=df[['director_name','num_critic_for_reviews']]

#left join
merged_left=pd.merge(subdf_1, subdf_2 , on="director_name", how='left')
print(merged_left)

#outer join
merged_outer=pd.merge(subdf_1,subdf_2,on='director_name',how='outer')
print(merged_outer)

#count
print('Left join row counts:',merged_left.shape[0])
print('Outer join row counts:',merged_outer.shape[0])
