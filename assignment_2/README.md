## Assignment 2 - Sentiment and NER

The script does the following:

Using the corpus of Fake vs Real news, write some code which does the following

-->Split the data into two datasets - one of Fake news and one of Real news

-->For every headline:

Get the sentiment scores

Find all mentions of geopolitical entites

Save a CSV which shows the text ID, the sentiment scores, and column showing all GPEs in that text

Find the 20 most common geopolitical entities mentioned across each dataset - plot the results as a bar charts


## Structure

This repository has the following directory structure:

| Column | Description|
|--------|:-----------|
```data```| a folder to be used for inputting the data you wish to run
```notebooks``` | Jupyter notebooks in both .ipynb and .html format
```src``` | the .py script version of the assignment
```output``` | the results of inputting the fake or real news dataset. The two bar charts are called real_bar_chart.png and fake_bar_chart.png. The csv's results are uploaded in a zip file as it is too big to upload

## Contribution

Sofie Thinggaard au613703

201909063@post.au.dk

## Methods

This problem relates to finding sentiment score and mentions of geopolitical entites (GPE) meaning locations, in the fake and real news dataset. In order to address this problem, we start with the whole dataset and splitting into real and fake news later. First, we rename column 0 (the unnamed column) to textID, then we make a list of all sentiment scores for every headline (the title column) in the dataset using Vader (thus a dictionary based approach), then getting it into a dataframe with columns that fits Vader's scoring system: "neg", "neu", "pos", "compound". Next, we combine the two dataframes: the one with textID and the sentiment dataframe. Now, we find mentions of geopolitical entites in headlines (the title column) and make a combined dataframe that consists of the headline and the GPE mentioned. We, again, combine dataframes: the one with sentiments and this new dataframe (the one with GPEs). We save to output folder as df_assign_2.csv. Because we want to include the sentiment scores on the headlines where there are no GPEs, we use an outer-join, getting NaNs (Not a number) where no GPE is found (inner-joining, on the other hand, will result in getting only entries where a GPE has been found in the title).
Next, we split the dataset into fake and real news, getting a dataframe for each with GPEs and sentiment for each headline. Then, we take the real news and count the GPEs and plot the 20 most frequently mentioned GPEs as a Bar Chart. We do the same with the fake news. We save the results as fake_bar_chart.png and real_bar_chart.png in the output folder.

## Usage (reproducing results)

In order to run this code, clone the repository and store the data in the data folder. You will need the packages in the requirements.txt document.

To replicate the results choose the dataset fake_or_real_news.csv

## Discussion of results

Results: getting a .csv file with the text ID, the sentiment scores, and column showing all GPEs in that text. Furthermore, two bar charts showing the 20 most frequently mentioned GPE split in real and fake news. Unfortunately, names like Obama will be counted as a GPE (this seems to have been changed/updated, so it is not the case anymore), however US and America are counted as seperate entities, a distinction that is perhaps not useful.

The most frequent GPEs in the fake news subset are US, Russia, America 

The most frequent GPEs in the real news subset are Iran, US, America

## Link to assignment 2 on GitHub

https://github.com/SofieThi/STH_Language/tree/main/assignment_2
