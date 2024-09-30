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
│   ├── data_appendix.pdf
│   └── new_movies.csv 
│
├── OUTPUT/
│   ├── Analysis/
│   │   ├── AverageSentimentScoreOverTime.png
│   │   ├── HeatmapNumericalFeatures.png
│   │   ├── PassByDecade.png
│   │   ├── PassFailvsSentimentScore.png
│   │   ├── ProportionOfMoviesPassingOverTime.png
│   │   ├── ScoreOfMoviesPassingVersusFailingOverTime.png
│   │   └── SentimentOverTimeBoxplot.png
│   └── Exploratory/
│       ├── DistributionofBechdelRatings.png
│       ├── DistributionofSentimentScores.png
│       ├── MoviesThatPassBechdel.png
│       ├── PairPlotYearSentimentRating.png
│       ├── PassOrFailBechdel.png
│       └── YearvsSentimentScore.png
│
├── SCRIPTS/
│   ├── 1-ScrapeNewBechdel.py
│   ├── 2-IMDbReviewSentiment.py
│   ├── 3-ExploratoryPlots.py
│   ├── 4-RoundSentiment.py
│   ├── 5-AddBinaryRating.py
│   ├── 6-LogisticRegression.py
│   ├── 7-HypothesisTesting.py
│   ├── 8-AnalysisPlots.py
│   └── 9-HypothesisTestingTime.py
│
├── LICENSE.md
└── README.md
```

- **DATA/**: Contains the various CSV files used throughout the project. These include the Bechdel movie datasets and sentiment data.
- **OUTPUT/**:
  - **Analysis/**: Folder to store the analysis results.
  - **Exploratory/**: Contains all the exploratory plots generated, such as sentiment and Bechdel test distributions.
- **SCRIPTS/**: Python scripts used in the project:
  - **1-ScrapeNewBechdel.py**: Script to scrape new movie data from the Bechdel test website.
  - **2-IMDbReviewSentiment.py**: Script to scrape IMDb reviews and calculate sentiment scores using VADER.
  - **3-ExploratoryPlots.py**: Script to generate exploratory visualizations.
  - **4-RoundSentiment.py**: Script to round the sentiment scores to 2 decimal places.
  - **5-AddBinaryRating.py**: Script to simplify the Bechdel rating into a pass/fail binary.
  - **6-LogisticRegression.py**: Script to perform logistic regression on the variables `rating_binary` and `sentiment`.
  - **7-HypothesisTesting.py**: Script to perform statistical tests on `rating_binary` and `sentiment`.
  - **8-AnalysisPlots.py**: Script to generate plots that allow for analysis of relationships between various variables in the **bechdel_movies.csv** file.
  - **9-HypothesisTestingTime.py**: Script to perform more hypothesis testing and output p-values.
  
---

## Section 3 - Instructions for Reproducing Results

Follow the steps below to reproduce the results of this project:

### Step 1: Dataset Collection
- Download the **Bechdel Test Dataset** from [Kaggle](https://www.kaggle.com/datasets/treelunar/bechdel-test-movies-as-of-feb-28-2023). This dataset includes over 9,000 movies, their Bechdel test ratings, and additional information such as the year of release.
- Place the downloaded CSV files in the **DATA/** folder of the project.

### Step 2: Gather Updated Bechdel Scores
- Use the **1-ScrapeNewBechdel.py** script to scrape the Bechdel test scores for movies added to the Bechdel test website from **February 2023 to the present**.
- This will gather the most recent Bechdel test ratings and add them to your dataset. Ensure that the scraped data is saved in the **bechdel_movies_combined.csv** file inside the **DATA/** folder.

### Step 3: Scrape IMDb Reviews
- Warning: This step can take up to an hour depending on the number of movies and the speed of your internet connection. IMDb may also limit the number of requests you can make in a short period.
- Use the **2-IMDbReviewSentiment.py** script to scrape reviews for each movie in the Bechdel test dataset. This script will gather around 15-20 reviews per movie using Python's `requests` and `BeautifulSoup` libraries.
- Ensure that IMDb allows you to scrape reviews by checking their terms of service before running the script.

### Step 4: Sentiment Analysis
- Run the **2-IMDbReviewSentiment.py** script to apply VADER sentiment analysis to the collected IMDb reviews. The script will output sentiment scores (positive, negative, neutral, and compound).
- The **compound sentiment score** is the main focus, and it will be added to the movie dataset.

### Step 5: Data Compilation and Exploratory Analysis
- Once the sentiment analysis is complete, the dataset containing Bechdel test results and the sentiment scores will be combined into a single CSV file, located in the **DATA/** folder.
- You can run **3-ExploratoryPlots.py** to generate various plots for exploratory data analysis, including distributions of Bechdel test ratings, sentiment scores, and a pair plot showing the relationships between `year`, `rating`, and `sentiment`.
- Run **5-AddBinaryRating.py** to simplify the `rating` variable into a binary pass/fail of the Bechdel test. This will make the next steps with hypothesis testing much easier.

### Step 6: Hypothesis Testing
- Use **6-LogisticRegression.py** to test the hypothesis that a movie passing the Bechdel test is more likely to have a positive sentiment score.
- The logistic regression model can be built using libraries like `sklearn` in Python, which will allow you to evaluate whether passing the Bechdel test significantly affects sentiment scores.
- Run the **7-HypothesisTesting.py**, **8-AnalysisPlots.py**, and **9-HypothesisTestingTime.py** files to generate more results and visualizations that will lead to the conclusion.
- The p-values generated in **9-HypothesisTestingTime.py** will be used to determine if there are statistically significant relationships between the chosen variables.
- The plots generated by **8-AnalysisPlots.py** help visualize the findings of the hypothesis testing.

### Optional Step: Rounding Sentiment Scores
- Use **4-RoundSentiment.py** to round the sentiment scores to two decimal places for easier interpretation.

By following these steps, you will be able to reproduce the data scraping, sentiment analysis, exploratory plots, and hypothesis testing used in this project.

---

## References 

[1] “vaderSentiment,” PyPI, Apr. 23, 2018. https://pypi.org/project/vaderSentiment/.

[2] “Bechdel Test Movies,” kaggle.com.
https://www.kaggle.com/datasets/treelunar/bechdel-test-movies-as-of-feb-28-2023

[3] Shih, J. (2024, July 3).Interpreting the score and ratio of sentiment analysis. Twinword.
https://www.twinword.com/blog/interpreting-the-score-and-ratio-ofsentiment/#:~:text=The%20score%20indicates%20how%20negative,inclusively%2C%20we%20tag%20as%20neutral

[4] J. Light, “What Is the Bechdel Test and How Will It Help Your Writing?,” nofilmschool.com, 
Jan. 25, 2024. https://nofilmschool.com/bechdel-test

[5] “Bechdel Test Movie List” bechdeltest.com
https://bechdeltest.com/

