# DS-4002-Project-1

## Section 1

The main softwares used for this project incldues google colab using python, and VS code with python. 
We used Python's request and BeautifulSoup packages to scrape the movie reviews from IMBd, and the VADER SentimentIntensityAnalyzer package to analyze the text reviews and get our sentiment scores.
Most of the coding was performed on a Windows machine, with some also being done using a Mac. 

## Section 2

## Section 3 

Step 1: Find our initial dataset
To begin collecting data to conduct our analysis, a dataset was found that included over 9,000 movies from various decades, each with a Bechdel test rating indicating whether the movie passed or failed the test. The dataset contains information on the Bechdel test results, such as whether the movie met the criteria (e.g., two named women, talking to each other, and not about a man), as well as the year of release. Once identifying this primary dataset, we focused on scraping reviews for the movies to compare their sentiment with the Bechdel test outcomes.

Step 2: scrape the IMDB movie review data
To begin collecting the sentiment data for the movies found in the Bechdel test dataset, around 15-20 reviews per movie were scraped from IMDb using Python, with a balance of both positive and negative reviews. These reviews were later used to generate the sentiment score for each movie using sentiment analysis techniques.

Step 3: Sentiment Analysis 
Each review, whether positive or negative, will be analyzed using the VADER sentiment analysis package in Python. In total, approximately 200,000 movie reviews will be analyzed to generate sentiment scores. The analysis will return positive, negative, neutral, and compound sentiment scores for each review. For this analysis, the compound sentiment score will be the key value added to the dataset for further evaluation.

Step 4: Data compilation into CSV and Exploratory Data Analysis
The information containing the Bechdel test results and the average sentiment score score from the movie reviews will be combined into a single data set. After appending the average sentiment score from each movie, the completed data set now has information about the movie release time, type of Bechdel test applied, budget information, and average sentiment score using the positive, negative, and neutral reviews.

Step 5: Hypothesis testing
The hypothesis that passing the Bechdel test will make the movie more likely to have a positive sentiment score will be tested by completing a logistical regression. Conducting a logistic regression analysis will allow for a prediction to be made if a movie that passes or fails the Bechdel test is more likely to have a positive, neutral, or negative sentiment score based on the given data. The goal is to have a statistically significant p value of less than 0.05, which will confirm or reject our hypothesis, H1. 
