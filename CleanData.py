import pandas as pd

# Load the dataset
file_path = './data/bechdel_movies_with_sentiment.csv'
df = pd.read_csv(file_path)

# List of columns to keep
columns_to_keep = ['title','imdb', 'year', 'decade code', 'binary', 'code', 'clean_test', 'average_sentiment', 'budget', 'domgross']

# Drop all other columns except the ones specified
df_filtered = df.loc[:, columns_to_keep]

# Update decade code for movies from 1980 to 1989 and 1970 to 1979
df_filtered.loc[(df_filtered['year'] >= 1980) & (df_filtered['year'] <= 1989), 'decade code'] = 4.0
df_filtered.loc[(df_filtered['year'] >= 1970) & (df_filtered['year'] <= 1979), 'decade code'] = 5.0

# Save the updated DataFrame to a new CSV file
output_file_path = './data/filtered_movies_updated.csv'
df_filtered.to_csv(output_file_path, index=False)

# Display the first few rows of the filtered dataframe
print(df_filtered.head())

