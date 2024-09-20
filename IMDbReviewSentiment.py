import pandas as pd
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from bs4 import BeautifulSoup
import time

# Download VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to fetch IMDb reviews for a movie
def fetch_imdb_reviews(imdbid):
    reviews = []
    url = f"https://www.imdb.com/title/tt{imdbid}/reviews?ref_=tt_ql_3"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract review texts from the IMDb reviews page
        review_texts = soup.find_all('div', class_='text show-more__control')
        
        for review in review_texts:
            reviews.append(review.get_text())
        
        return reviews if reviews else None
    
    except requests.exceptions.HTTPError as error:
        print(f"Error fetching reviews for IMDb ID {imdbid}: {error}")
        return None

# Function to calculate average sentiment score
def calculate_average_sentiment(reviews):
    if not reviews:
        return None  # No reviews found
    
    sentiment_scores = [analyzer.polarity_scores(review)['compound'] for review in reviews]
    
    return sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else None

# Load the dataset
df = pd.read_csv('./data/bechdel_movies_combined.csv')

# Ensure IMDb IDs are properly formatted (should be a string with 7 or more digits)
df['imdbid'] = df['imdbid'].apply(lambda x: str(x).zfill(7))

# Function to fetch and process sentiment for a single movie
def process_movie(row, idx, total):
    imdbid = row['imdbid']
    reviews = fetch_imdb_reviews(imdbid)
    
    if reviews:
        sentiment = calculate_average_sentiment(reviews)
    else:
        sentiment = None
    
    # Print progress
    print(f"Processed movie {idx + 1}/{total}")
    
    return sentiment

# Use ThreadPoolExecutor to parallelize the processing of movies
def process_movies_concurrently(df, max_workers=10):
    sentiment_scores = [None] * len(df)
    total_movies = len(df)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_movie, row, idx, total_movies): idx for idx, row in df.iterrows()}
        
        for future in as_completed(futures):
            idx = futures[future]
            try:
                sentiment_scores[idx] = future.result()
            except Exception as e:
                print(f"Error processing row {idx}: {e}")
    
    return sentiment_scores

# Fetch sentiment scores concurrently
sentiment_scores = process_movies_concurrently(df)

# Add the sentiment scores to the dataframe
df['sentiment'] = sentiment_scores

# Save the updated dataframe
df.to_csv('./data/bechdel_movies_with_sentiment.csv', index=False)

# Preview the updated dataframe
df.head()
