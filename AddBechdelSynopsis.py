import pandas as pd
from imdb import IMDb
from concurrent.futures import ThreadPoolExecutor

# Load the dataset
file_path = './data/bechdel_movies.csv'
df = pd.read_csv(file_path)

# Initialize IMDb object
ia = IMDb()

# Function to retrieve synopsis for a given IMDb ID
def get_movie_synopsis(imdb_id):
    print("started")
    try:
        # Get the movie object by IMDb ID
        movie = ia.get_movie(imdb_id[2:])  # remove 'tt' from the start of IMDb ID
        # Get the synopsis, fallback to plot outline if synopsis not available
        synopsis = movie.get('plot outline') or movie.get('synopsis', [''])[0]
        print("finished good")
        return synopsis
    except Exception as e:
        print(f"Error fetching synopsis for {imdb_id}: {e}")
        return None

# Function to fetch synopsis in parallel
def fetch_synopsis_in_parallel(imdb_ids):
    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers for your machine
        synopses = list(executor.map(get_movie_synopsis, imdb_ids))
    return synopses

# Fetch the synopsis for all movies in parallel
df['synopsis'] = fetch_synopsis_in_parallel(df['imdb'])

# Save the updated DataFrame to a new CSV file
output_file_path = './data/bechdel_movies_with_synopsis.csv'
df.to_csv(output_file_path, index=False)

print(f"Updated dataset saved to {output_file_path}")
