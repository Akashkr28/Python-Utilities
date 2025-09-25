import os
import json

FILENAME = 'movies.json'

def load_movies():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)
    
def save_movies(movies):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2)

def add_movies(movies):
    title = input("Enter movie title: ").strip().lower()

    if any(movie["title"].lower() == title for movie in movies):
        print("Movie already exists in the list.")
        return
    genre = input("Enter movie genre: ").strip().lower()
    try:
        rating = float(input("Enter movie rating (1-10): "))
        if not (0 <= rating <=10):
            raise ValueError
    except ValueError:
        print("Please enter a valid rating between 1 and 10.")
        return
    
    movies.append({
        "title": title,
        "genre": genre,
        "rating": rating
    })
    save_movies(movies)
    print("Movies added 🎬")

def search_movies(movies):
    term = input("Enter the title or genre: ").strip().lower()

    results = [movie for movie in movies 
     if term in movie["title"].lower() or term in movie
     ['genre'].lower() 
          
    ]
    if not results:
        print("No movies found.")
        return
    print(f"Found {len(results)} result(s): ")

    for movie in results:
        print(f"{movie['title']} -- {movie["genre"]} -- {movie["rating"]}")

def view_movies(movies):
    if not movies:
        print("No movies in the database.")
        return
    for movie in movies:
        print(f"{movie['title']} -- {movie['genre']} -- {movie['rating']}")
    print("=" * 30)


def run_movie_db():
    movies = load_movies()

    while True:
        print("\n 🍿 MyMovieDB")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie")
        print("4. Exit")

        choice = input("Choose an options (1-4): ").strip()
        match choice:
            case "1": add_movies(movies)
            case "2": view_movies(movies)
            case "3": search_movies(movies)
            case "4": break
            case _: print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    run_movie_db()