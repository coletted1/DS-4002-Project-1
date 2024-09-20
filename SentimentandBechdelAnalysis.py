import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = './data/bechdel_movies_with_sentiment.csv'
data = pd.read_csv(file_path)

# 1. Violin Plot: Distribution of Sentiment by Bechdel Test Result
plt.figure(figsize=(10, 6))
sns.violinplot(data=data, x='binary', y='average_sentiment', palette='coolwarm')
plt.title('Distribution of IMDb Sentiment by Bechdel Test Result')
plt.xlabel('Bechdel Test Result')
plt.ylabel('Average Sentiment Score')
plt.show()

# 2. KDE Plot: Sentiment Density for PASS vs FAIL
plt.figure(figsize=(10, 6))
sns.kdeplot(data=data[data['binary'] == 'PASS']['average_sentiment'], label='PASS', shade=True, color='blue')
sns.kdeplot(data=data[data['binary'] == 'FAIL']['average_sentiment'], label='FAIL', shade=True, color='red')
plt.title('Density Plot of Sentiment for Bechdel Test PASS vs FAIL')
plt.xlabel('Average Sentiment Score')
plt.ylabel('Density')
plt.legend(title='Bechdel Test Result')
plt.show()

# 3. Sentiment Boxplot: Grouped by Decades and Bechdel Test Result
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, x='decade code', y='average_sentiment', hue='binary', palette='coolwarm')
plt.title('Sentiment Scores by Decade and Bechdel Test Result')
plt.xlabel('Decade')
plt.ylabel('Average Sentiment Score')
plt.legend(title='Bechdel Test Result')
plt.show()

# 4. Histogram: Sentiment Score Distribution by Bechdel Test Result
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='average_sentiment', hue='binary', multiple='stack', palette='coolwarm', bins=20)
plt.title('Histogram of Sentiment Scores Grouped by Bechdel Test Result')
plt.xlabel('Average Sentiment Score')
plt.ylabel('Count')
plt.legend(title='Bechdel Test Result')
plt.show()

# 5. Mean Sentiment by Bechdel Test Result
mean_sentiment_by_bechdel = data.groupby('binary')['average_sentiment'].mean().reset_index()

plt.figure(figsize=(8, 6))
sns.barplot(data=mean_sentiment_by_bechdel, x='binary', y='average_sentiment', palette='coolwarm')
plt.title('Mean Sentiment by Bechdel Test Result')
plt.xlabel('Bechdel Test Result')
plt.ylabel('Mean Average Sentiment Score')
plt.show()
