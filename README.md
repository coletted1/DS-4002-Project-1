# DS-4002-Project-1 

## Section 1 - Software & Platform

The main software used for this project includes Google Colab with Python and VS Code with Python. We used Python's **requests** and **BeautifulSoup** packages to scrape movie reviews from IMDb, and the **VADER SentimentIntensityAnalyzer** package to analyze the text reviews and derive sentiment scores. 

Most coding was performed on a Windows machine, with some portions done using a Mac.

---

## Section 2 - Map of Documentation

### Project Folder Structure:

```
DS-4002-Project-1/
│
├── DATA/
│   ├── bechdel_movies_2023_FEB.csv
│   ├── bechdel_movies_combined.csv
│   ├── bechdel_movies_with_sentiment.csv
│   ├── bechdel_movies.csv
│   └── new_movies.csv
│
├── OUTPUT/
│   ├── Analysis/
│   │   └── (analysis results saved here)
│   └── Exploratory/
│       ├── DistributionofBechdelRatings.png
│       ├── DistributionofSentimentScores.png
│       ├── MoviesThatPassBechdel.png
│       ├── PairPlotKey.png
│       ├── PairPlotYearSentimentRating.png
│       ├── PassOrFailBechdel.png
│       └── YearvsSentimentScore.png
│
├── SCRIPTS/
│   ├── ExploratoryPlots.py
│   ├── IMDbReviewSentiment.py
│   ├── RoundSentiment.py
│   └── ScrapeNewBechdel.py
│
├── LICENSE.md
└── README.md
```

- **DATA/**: Contains the various CSV files used throughout the project. These include the Bechdel movie datasets and sentiment data.
- **OUTPUT/**:
  - **Analysis/**: Folder to store the analysis results.
  - **Exploratory/**: Contains all the exploratory plots generated, such as sentiment and Bechdel test distributions.
- **SCRIPTS/**: Python scripts used in the project:
  - **ExploratoryPlots.py**: Script to generate exploratory visualizations.
  - **IMDbReviewSentiment.py**: Script to scrape IMDb reviews and calculate sentiment scores using VADER.
  - **RoundSentiment.py**: Script to round the sentiment scores to 2 decimal places.
  - **ScrapeNewBechdel.py**: Script to scrape new movie data from the Bechdel test website.
  
---

## Section 3 - Instructions for Reproducing Results

Follow the steps below to reproduce the results of this project:

### Step 1: Dataset Collection
- Download the **Bechdel Test Dataset** from [Kaggle](https://www.kaggle.com/datasets/treelunar/bechdel-test-movies-as-of-feb-28-2023). This dataset includes over 9,000 movies, their Bechdel test ratings, and additional information such as the year of release.
- Place the downloaded CSV files in the **DATA/** folder of the project.

### Step 2: Gather Updated Bechdel Scores
- Use the **ScrapeNewBechdel.py** script to scrape the Bechdel test scores for movies added to the Bechdel test website from **February 2023 to the present**.
- This will gather the most recent Bechdel test ratings and add them to your dataset. Ensure that the scraped data is saved in the **bechdel_movies_combined.csv** file inside the **DATA/** folder.

### Step 3: Scrape IMDb Reviews
- Use the **IMDbReviewSentiment.py** script to scrape reviews for each movie in the Bechdel test dataset. This script will gather around 15-20 reviews per movie using Python's `requests` and `BeautifulSoup` libraries.
- Ensure that IMDb allows you to scrape reviews by checking their terms of service before running the script.

### Step 4: Sentiment Analysis
- Run the **IMDbReviewSentiment.py** script to apply VADER sentiment analysis to the collected IMDb reviews. The script will output sentiment scores (positive, negative, neutral, and compound).
- The **compound sentiment score** is the main focus, and it will be added to the movie dataset.

### Step 5: Data Compilation and Exploratory Analysis
- Once the sentiment analysis is complete, the dataset containing Bechdel test results and the sentiment scores will be combined into a single CSV file, located in the **DATA/** folder.
- You can run **ExploratoryPlots.py** to generate various plots for exploratory data analysis, including distributions of Bechdel test ratings, sentiment scores, and a pair plot showing the relationships between `year`, `rating`, and `sentiment`.

### Step 6: Hypothesis Testing
- Use logistic regression to test the hypothesis that a movie passing the Bechdel test is more likely to have a positive sentiment score.
- The logistic regression model can be built using libraries like `sklearn` in Python, which will allow you to evaluate whether passing the Bechdel test significantly affects sentiment scores.

### Optional Step: Rounding Sentiment Scores
- Use **RoundSentiment.py** to round the sentiment scores to two decimal places for easier interpretation.

By following these steps, you will be able to reproduce the data scraping, sentiment analysis, exploratory plots, and hypothesis testing used in this project.

---

## References 

[1] “vaderSentiment,” PyPI, Apr. 23, 2018. https://pypi.org/project/vaderSentiment/.

[3] “Bechdel Test Movies,” kaggle.com.
https://www.kaggle.com/datasets/treelunar/bechdel-test-movies-as-of-feb-28-2023

[4] Shih, J. (2024, July 3).Interpreting the score and ratio of sentiment analysis. Twinword.
https://www.twinword.com/blog/interpreting-the-score-and-ratio-of-sentiment/#:~:text=The%20sc
ore%20indicates%20how%20negative,inclusively%2C%20we%20tag%20as%20neutral

[5] J. Light, “What Is the Bechdel Test and How Will It Help Your Writing?,” nofilmschool.com, 
Jan. 25, 2024. https://nofilmschool.com/bechdel-test

[6] “Bechdel Test Movie List” bechdeltest.com
https://bechdeltest.com/

