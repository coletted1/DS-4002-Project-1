# Load the new dataset that contains the synopsis
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon (only needed the first time)
nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Load the dataset
file_path = './data/bechdel_movies_with_synopsis.csv'
df = pd.read_csv(file_path)

# Function to perform sentiment analysis on the synopsis
def analyze_sentiment(synopsis):
    if isinstance(synopsis, str):  # Ensure the synopsis is a valid string
        sentiment = sid.polarity_scores(synopsis)
        return sentiment['compound']  # Return the compound sentiment score
    return None

# Apply sentiment analysis to the 'synopsis' column
df['synopsis_sentiment'] = df['synopsis'].apply(analyze_sentiment)

# Save the updated DataFrame to a new CSV file
output_file_path = './data/bechdel_movies_with_sentiment.csv'
df.to_csv(output_file_path, index=False)

output_file_path  # Return the path to the updated file with sentiment scores