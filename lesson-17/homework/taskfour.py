import pandas as pd

#reading from csv filter
df=pd.read_csv('movie.csv')

#creating grouped dataframe(color+director_name)
grouped=df.groupby(['color','director_name']).agg({
    'num_critic_for_reviews':'sum',
    'duration':'mean'
})

#creating new dataframe
grouped.columns=['TotalCritics','AverageDuration']
grouped=grouped.reset_index()
print(grouped)

