import pandas as pd

# Load the dataset
df = pd.read_csv('./data/bechdel_movies_with_sentiment.csv')

# Round the sentiment column to two decimal places
df['sentiment'] = df['sentiment'].round(2)

# Save the updated dataframe to a new CSV file
df.to_csv('./data/bechdel_movies_with_sentiment.csv', index=False)

# Optional: Preview the first few rows to confirm changes
print(df.head())
