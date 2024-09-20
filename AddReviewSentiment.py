import requests
from bs4 import BeautifulSoup
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Download the Vader lexicon (if not already downloaded)
nltk.download('vader_lexicon')

# Initialize the SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

# Function to scrape IMDb reviews for a movie based on its IMDb ID
def get_imdb_reviews(imdb_id):
    url = f"https://www.imdb.com/title/{imdb_id}/reviews"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch reviews for {imdb_id}")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the review text on the page
    reviews = soup.find_all('div', class_='text show-more__control')
    review_texts = [review.get_text() for review in reviews]

    return review_texts

# Function to get the sentiment scores for a list of reviews
def analyze_sentiment(reviews):
    sentiments = []
    for review in reviews:
        sentiment_score = sid.polarity_scores(review)
        sentiments.append(sentiment_score['compound'])  # Compound is an overall sentiment score
    return sentiments

# Function to process each movie: scrape reviews, analyze sentiment, and calculate average sentiment
def scrape_and_analyze(imdb_id):
    reviews = get_imdb_reviews(imdb_id)
    
    if reviews:
        # Perform sentiment analysis on the reviews
        sentiment_scores = analyze_sentiment(reviews)
        
        # Calculate the average sentiment score
        average_sentiment = sum(sentiment_scores) / len(sentiment_scores)
        return imdb_id, average_sentiment
    return imdb_id, None  # If no reviews are found, return None

# Load the dataset
file_path = './data/bechdel_movies.csv'
df = pd.read_csv(file_path)

# Add a column for average sentiment scores
df['average_sentiment'] = None

# Limit the number of threads to avoid overwhelming IMDb's servers
max_threads = 10

# Use ThreadPoolExecutor to parallelize the scraping and analysis
with ThreadPoolExecutor(max_workers=max_threads) as executor:
    futures = [executor.submit(scrape_and_analyze, row['imdb']) for index, row in df.iterrows()]
    
    for future in as_completed(futures):
        imdb_id, avg_sentiment = future.result()
        # Update the dataframe with the result
        df.loc[df['imdb'] == imdb_id, 'average_sentiment'] = avg_sentiment
        print(f"Processed {imdb_id} with average sentiment: {avg_sentiment}")

# Save the updated dataframe with sentiment analysis
output_file = './data/bechdel_movies_with_sentiment.csv'
df.to_csv(output_file, index=False)

print(f"Sentiment analysis added to the dataset and saved to {output_file}.")
