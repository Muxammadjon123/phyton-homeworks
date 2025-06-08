import requests
import random

api_key = "6c4b6613683f702ce9cb11271dfe99d4"

def get_genres():
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        genres = response.json().get("genres", [])
        return {genre['name'].lower(): genre['id'] for genre in genres}
    else:
        print("Failed to get genres")
        return {}

def get_movies_by_genre(genre_id):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get("results", [])
        return results
    else:
        print("Failed to get movies")
        return []

def main():
    genres = get_genres()
    if not genres:
        return

    print("Available genres:")
    for name in genres.keys():
        print(f"- {name.capitalize()}")

    user_genre = input("Enter a movie genre from the list above: ").strip().lower()
    if user_genre not in genres:
        print("Genre not found.")
        return

    genre_id = genres[user_genre]
    movies = get_movies_by_genre(genre_id)
    if not movies:
        print("No movies found for this genre.")
        return

    movie = random.choice(movies)
    title = movie.get('title')
    overview = movie.get('overview', 'No description available.')
    release_date = movie.get('release_date', 'N/A')

    print(f"\nRecommended {user_genre.capitalize()} movie:")
    print(f"Title: {title}")
    print(f"Release Date: {release_date}")
    print(f"Overview: {overview}")

if __name__ == "__main__":
    main()
