## self-assigned project: Testing the sentiment-roberta-large-english model on IMDB movie reviews

-use the sentiment-roberta-large-english model on the IMDB movie reviews dataset

-data proprocessing: convert the labels into ones and zeros, exclude reviews that are too long for the model to do sentiment analysis on

-how well the model is performing? Make a classification report and save it to the output folder

-Is the model better at predicting negative or positive sentiments? Make a confusion_matrix and save it to the output folder


## Structure

This repository has the following directory structure:

| Column | Description|
|--------|:-----------|
```data```| a folder to be used for inputting the data you wish to run
```notebooks``` | Jupyter notebooks in both .ipynb and .html format
```src``` | the .py script version of the assignment
```output``` | the results of inputting the dataset. The lassification report is called ... and the confusion matrix ...

## Contribution

Sofie Thinggaard au613703

201909063@post.au.dk

## Methods

This problem relates to finding how well a pretrained model (sentiment-roberta-large-english) works on prelabeled data (IMDB reviews). The data consists of movie reviews that has has been labelled positive or negative according to sentiment. In order to address this problem, we first find the models and define the URL as MODEL. Then we initalize a pretrained tokenizer and the model and load the prelabelled dataset. We need to convert the labels (negative and positive) into ones and zeros to match the model. Because the dataset is so large, I make it smaller (subset of 500 reviews), it can be commented out however, and the full 50000 reviews can be used. Next, we make a pipeline to quickly generate results. Now, there is a problem with the lengths of some of the reviews in the dataset: some are too long for the model to do sentiment analysis on, hence, we make a list of the reviews it is able to score and another list with the reviews that are too long. Then, we make a list keeping only the prediction (negative or positive) and make it lowercase to match the model. Then, we make a list with only the scored labels in our data. We generate a classification report to get an overview of how well the model is performing and save it in output folder, and to find out if the model is better at predicting negative or positive sentiments, we make a confusion matrix and save to an output folder.

## Usage (reproducing results)

In order to run this code, clone the repository and store the data in the data folder. You will need the packages in the requirements.txt document. 

To replicate the results chose the first 500 reviews in the IMDB dataset from kaggle: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews and use the model from Huggingface https://huggingface.co/siebert/sentiment-roberta-large-english

## Discussion of results

Results: getting a classification report and a confusion matrix to see how well the model is performing. Using pretrained models both reduce time and computer effort since we do not have to build and compile the models ourselves, and the pretrained model is performing very well, getting an accuracy of 97%. The Siebert model has been fine-tuned on datasets from different types of texts in order to increase its ability to generalize, and it seemingly does its job well on its specific job: to predict either positive/1 or negative/0 sentiment.

The confusion matrix would yield clearer results had the movie reviews sentiment's been equally divided between positive and negative. They are not however, with more negative reviews than positive. However, the confusion matrix reveals that the model predicts very few wrong in both sentiment cases (it does not overly predict wrong in one case or the other).
