import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = './data/bechdel_movies_with_sentiment.csv'
data = pd.read_csv(file_path)

# 1. Scatterplot: Average Sentiment vs Budget (Does Passing the Bechdel Test Affect Budget?)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='budget_2013$', y='average_sentiment', hue='binary', palette='coolwarm')
plt.title('Sentiment vs Budget (2013 $) by Bechdel Test Result')
plt.xlabel('Budget (2013 $)')
plt.ylabel('Average Sentiment Score')
plt.legend(title='Bechdel Test Result')
plt.show()

# 2. Scatterplot: Average Sentiment vs Domestic Gross Revenue (Impact of Bechdel Test Passing on Domestic Revenue)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='domgross_2013$', y='average_sentiment', hue='binary', palette='coolwarm')
plt.title('Sentiment vs Domestic Gross Revenue (2013 $) by Bechdel Test Result')
plt.xlabel('Domestic Gross Revenue (2013 $)')
plt.ylabel('Average Sentiment Score')
plt.legend(title='Bechdel Test Result')
plt.show()

# 3. Pairplot: Correlation Between Sentiment, Budget, and Gross Revenue (Bechdel Test Result as Hue)
sns.pairplot(data[['average_sentiment', 'budget_2013$', 'domgross_2013$', 'intgross_2013$', 'binary']], hue='binary', palette='coolwarm')
plt.suptitle('Pairwise Relationships Between Sentiment, Budget, and Gross Revenue')
plt.show()

# 4. Correlation Heatmap: Numeric Variables (Including Sentiment, Budget, and Revenue)
plt.figure(figsize=(10, 8))
correlation_matrix = data[['average_sentiment', 'budget_2013$', 'domgross_2013$', 'intgross_2013$', 'year']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Sentiment, Budget, Revenue, and Year')
plt.show()

# 5. Barplot: Average Sentiment by Decade and Bechdel Test Result
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='decade code', y='average_sentiment', hue='binary', palette='coolwarm')
plt.title('Average Sentiment by Decade and Bechdel Test Result')
plt.xlabel('Decade')
plt.ylabel('Average Sentiment Score')
plt.legend(title='Bechdel Test Result')
plt.show()
