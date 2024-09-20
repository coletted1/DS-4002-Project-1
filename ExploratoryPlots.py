import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
file_path = './data/bechdel_dataset.csv'
bechdel_data = pd.read_csv(file_path)

# Ensure the plots are displayed in an appealing manner
sns.set(style="whitegrid", palette="bright")

# Plot 1: How many movies per year are in the dataset
plt.figure(figsize=(10, 6))
movies_per_year = bechdel_data.groupby('year')['title'].count()
movies_per_year.plot(kind='bar', color='tab:blue')
plt.title('Movies Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.show()

# Plot 2: Sentiment of movie reviews over the years
plt.figure(figsize=(10, 6))
sns.lineplot(data=bechdel_data, x='year', y='average_sentiment', marker='o', color='tab:green')
plt.title('Sentiment of Movie Reviews Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Sentiment')
plt.show()

# Plot 3: Movies that pass the Bechdel test from 1970-2013
bechdel_data['passes_bechdel'] = bechdel_data['binary'] == 'PASS'
movies_1970_2013 = bechdel_data[(bechdel_data['year'] >= 1970) & (bechdel_data['year'] <= 2013)]
movies_bechdel_pass = movies_1970_2013.groupby('year')['passes_bechdel'].sum()

plt.figure(figsize=(10, 6))
movies_bechdel_pass.plot(kind='bar', color='tab:orange')
plt.title('Movies Passing Bechdel Test (1970-2013)')
plt.xlabel('Year')
plt.ylabel('Number of Movies Passing')
plt.show()

# Plot 4: Relationship between variables in the dataset (Budget vs Domestic Gross by Bechdel Test Result)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=bechdel_data, x='budget', y='domgross', hue='binary', palette="Set1")
plt.title('Budget vs Domestic Gross by Bechdel Test Result')
plt.xlabel('Budget')
plt.ylabel('Domestic Gross')
plt.show()
