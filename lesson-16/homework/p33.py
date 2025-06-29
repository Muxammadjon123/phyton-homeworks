import pandas as pd

df=pd.read_csv('movie.csv')

director_likes = df.groupby('director_name')['director_facebook_likes'].sum()

top_director = director_likes.idxmax()
top_likes = director_likes.max().astype(int)

print(f"Director with the highest total likes: {top_director} ({top_likes} likes)")


top_5_longest = df[['movie_title', 'duration', 'director_name']].sort_values(by='duration', ascending=False).head(5)
print(f'Top 5 longest movies\n{top_5_longest}')
