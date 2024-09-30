import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset again and clean as before
file_path = './data/bechdel_movies.csv'
df = pd.read_csv(file_path)

df_clean = df.dropna(subset=['sentiment'])

# Convert the 'year' column to numeric format
df_clean['year'] = pd.to_numeric(df_clean['year'], errors='coerce')

# 1. Bechdel Test Results Over Time
# Calculate the proportion of movies passing the Bechdel test by year
bechdel_by_year = df_clean.groupby('year')['rating_binary'].mean()

# 2. Sentiment Score Over Time
sentiment_by_year = df_clean.groupby('year')['sentiment'].mean()

# Plot Bechdel Test Results Over Time
plt.figure(figsize=(10, 6))
plt.plot(bechdel_by_year.index, bechdel_by_year, label='Proportion Passing Bechdel Test', color='b')
plt.title('Proportion of Movies Passing the Bechdel Test Over Time')
plt.xlabel('Year')
plt.ylabel('Proportion Passing')
plt.grid(True)
plt.legend()
plt.show()

# Plot Sentiment Score Over Time
plt.figure(figsize=(10, 6))
plt.plot(sentiment_by_year.index, sentiment_by_year, label='Average Sentiment Score', color='g')
plt.title('Average Sentiment Score of Movies Over Time')
plt.xlabel('Year')
plt.ylabel('Sentiment Score')
plt.grid(True)
plt.legend()
plt.show()

# 3. Sentiment Score for Pass/Fail Over Time
plt.figure(figsize=(10, 6))
df_clean.groupby(['year', 'rating_binary'])['sentiment'].mean().unstack().plot(ax=plt.gca())
plt.title('Average Sentiment Score of Movies Passing vs Failing the Bechdel Test Over Time')
plt.xlabel('Year')
plt.ylabel('Sentiment Score')
plt.grid(True)
plt.legend(['Failing', 'Passing'])
plt.show()
