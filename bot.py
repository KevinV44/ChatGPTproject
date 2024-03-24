# Import necessary libraries
import requests

# Function to fetch movie recommendations from IMDb
def get_movie_recommendations(user_preferences):
    imdb_api_key = 'your_imdb_api_key_here'
    base_url = 'https://api.themoviedb.org/3/discover/movie'
    
    params = {
        'api_key': c661d5c888c0835cfd6d2b38d7f0562d,
        'with_genres': user_preferences['genre'],
        'with_cast': user_preferences['actor'],
        'sort_by': 'popularity.desc'
    }
    
    response = requests.get(base_url, params=params)
    recommended_movies = response.json()['results']
    
    return recommended_movies

# Function to process user input and generate recommendations
def generate_movie_recommendations():
    user_preferences = {
        'genre': input('Enter your favorite movie genre: '),
        'actor': input('Enter your favorite actor or actress: ')
    }
    
    recommendations = get_movie_recommendations(user_preferences)
    
    print('Top movie recommendations for you:')
    for movie in recommendations:
        print(movie['title'])

# Main function
if __name__ == '__main__':
    generate_movie_recommendations()
