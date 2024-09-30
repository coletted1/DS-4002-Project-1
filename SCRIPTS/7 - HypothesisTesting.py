# Re-import the necessary data
import pandas as pd
from scipy.stats import ttest_ind, mannwhitneyu

# Load the dataset again and clean as before
file_path = './data/bechdel_movies.csv'
df = pd.read_csv(file_path)

# Simplify the 'rating' column into binary classification: 1 for pass (rating == 3), 0 for fail (rating != 3)
df['rating_binary'] = df['rating'].apply(lambda x: 1 if x == 3 else 0)

# Drop rows with missing sentiment values
df_clean = df.dropna(subset=['sentiment'])

# Split the data into two groups: movies that pass and movies that fail the Bechdel test
pass_group = df_clean[df_clean['rating_binary'] == 1]['sentiment']
fail_group = df_clean[df_clean['rating_binary'] == 0]['sentiment']

# Perform a two-sample t-test (parametric)
t_stat, p_value_ttest = ttest_ind(pass_group, fail_group, nan_policy='omit')

# Perform Mann-Whitney U test (non-parametric)
u_stat, p_value_mannwhitney = mannwhitneyu(pass_group, fail_group, alternative='two-sided')

# Output results
print(p_value_ttest, p_value_mannwhitney)
