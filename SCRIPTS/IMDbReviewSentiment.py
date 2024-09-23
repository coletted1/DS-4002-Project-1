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

# Function to fetch IMDb reviews
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
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching reviews for IMDb ID {imdbid}: {e}")
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

# Function to process a batch of movies concurrently
def process_batch(batch_df, max_workers=10):
    sentiment_scores = [None] * len(batch_df)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch_imdb_reviews, row['imdbid']): idx for idx, (index, row) in enumerate(batch_df.iterrows())}
        
        for future in as_completed(futures):
            idx = futures[future]  # This is now the relative index within the batch
            try:
                reviews = future.result()
                sentiment_scores[idx] = calculate_average_sentiment(reviews)
            except Exception as e:
                print(f"Error processing row {idx}: {e}")
    
    return sentiment_scores

# Split the dataset into batches and process each batch
def process_movies_in_batches(df, batch_size=100, max_workers=10):
    total_movies = len(df)
    sentiment_scores = []

    for batch_start in range(0, total_movies, batch_size):
        batch_df = df.iloc[batch_start:batch_start + batch_size]
        print(f"Processing batch: {batch_start + 1} to {batch_start + len(batch_df)}")
        
        # Process the batch concurrently
        batch_sentiment_scores = process_batch(batch_df, max_workers)
        sentiment_scores.extend(batch_sentiment_scores)
        
        # Optional: Small delay between batches to avoid overwhelming the server
        time.sleep(10)  # Adjust as needed to avoid rate-limiting (optional)
    
    return sentiment_scores

# Fetch sentiment scores in batches
sentiment_scores = process_movies_in_batches(df, batch_size=100, max_workers=10)

# Add the sentiment scores to the dataframe
df['sentiment'] = sentiment_scores

# Save the updated dataframe
df.to_csv('.DATA/bechdel_movies_with_sentiment.csv', index=False)

# Preview the updated dataframe
df.head()
