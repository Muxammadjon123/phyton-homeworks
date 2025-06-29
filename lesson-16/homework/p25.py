import pandas as pd


df=pd.read_csv('movie.csv')
df_filtered=df[df['duration']>120]

sorted_df =df_filtered.sort_values(by='director_facebook_likes', ascending=False)

print(sorted_df)