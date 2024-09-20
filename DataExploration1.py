import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = './data/bechdel_movies_with_sentiment.csv'
data = pd.read_csv(file_path)

# Plot 1: Distribution of Bechdel Test Results (PASS/FAIL)
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='binary', palette='coolwarm')
plt.title('Distribution of Bechdel Test Results')
plt.xlabel('Bechdel Test Result')
plt.ylabel('Count')
plt.show()

# Plot 2: Sentiment Score Distribution by Bechdel Test Result
plt.figure(figsize=(8, 6))
sns.boxplot(data=data, x='binary', y='average_sentiment', palette='coolwarm')
plt.title('Sentiment Score Distribution by Bechdel Test Result')
plt.xlabel('Bechdel Test Result')
plt.ylabel('Average Sentiment Score')
plt.show()

# Plot 3: Average Sentiment Score Over Time
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='year', y='average_sentiment', marker='o', ci=None)
plt.title('Average Sentiment Score Over Time')
plt.xlabel('Year')
plt.ylabel('Average Sentiment Score')
plt.show()

# Plot 4: Sentiment Score Over Time by Bechdel Test Result
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='year', y='average_sentiment', hue='binary', marker='o', ci=None, palette='coolwarm')
plt.title('Sentiment Score Over Time by Bechdel Test Result')
plt.xlabel('Year')
plt.ylabel('Average Sentiment Score')
plt.legend(title='Bechdel Test Result')
plt.show()
