## Assignment 4 - Text classification

The two scripts do the following:

-->The first script should perform benchmark classification using standard machine learning approaches

This means TfidfVectorizer(), LogisticRegression classifier

Save the results from the classification report to a text file

-->The second script should perform classification using the kind of deep learning methods we saw in class

Keras Embedding layer, Convolutional Neural Network

Save the classification report to a text file

## Structure

This repository has the following directory structure:

| Column | Description|
|--------|:-----------|
```data```| a folder to be used for inputting the data you wish to run
```notebooks``` | Jupyter notebooks in both .ipynb and .html format
```src``` | the .py script version of the assignments. The first script is called assign_lr.py, the second script is called assign_dl.py
```output``` | the results of inputting the toxic dataset. The first script's output is benchmark_assign_4.txt, the second script is deep_learning_assign_4.txt
```utils``` | premade script with premade functions with tools for data munging

## Contribution

Sofie Thinggaard au613703

201909063@post.au.dk

## Methods

This problem relates to text classification. We are going to train a model to predict whether or not a comment is toxic or non-toxic. The first script: assign_lr.py performs benchmark classification using standard machine learning approaches (TfidfVectorizer and Logistic Regression classifier). Firstly, we create more balanced dataset by getting a random sample of the dataset (1000 datapoints), then we create new variables called text and label, then we do a train-test split, create vectorizer object using TfidfVectorizer, this vectorizer is then used to turn all of our documents into a vector of numbers instead of text. Then, we classify and predict with Logistic Regression. We make a classification report and save it to an output folder. 

The second script: assign_dl.py performs classification using deep learning methods with Keras Embedding layer and Convolutional Neural Network. Firstly, we create new variables called text and label, do a train-test split, clean and normalize data (lots of noise in the data like html tags), then we define what to do if model encounter unknown words it has not seen during training with: UNK, we fit tokenizer on the documents, we set a padding value because we have different lengths of documents, so need a max document length. If shorter we pad with zeros. We then tokenize all documents using this fit tokenizer, we do a sequence normalization (sequence= anything that can be iterated over), we add padding to sequences, we encode labels, we define parameters for the model and create it and train it. Finally, we can evaluate and make a classification report and save to an output folder.

## Usage (reproducing results)

In order to run this code, clone the repository and store the data in the data folder. You will need the packages in the requirements.txt document.

To replicate the results chose the dataset VideoCommentsThreatCorpus.csv from https://www.simula.no/sites/default/files/publications/files/cbmi2019_youtube_threat_corpus.pdf 

## Discussion of results

Results: Getting two text documents with two classification reports showing how good each model is at predicting whether a comment is toxic/1 or non toxic/0

The first script with the LogisticRegression classifier (assign_lr.py) had an accuracy of 72%. Unsurprisingly, this simpler model's accuracy is worse than the deep learning model. This model uses vectorization in order to represent the text input, but it does not account for how words are related or positioned.

The second script with the classification using deep learning methods (assign_dl.py), and had a higher accuracy score with 97%. This is because, with deep learning methods, you also need to convert the text to numbers (a numerical representation), however this model takes positional information into account. The most efficient way is with word embeddings, since it gives valuable linguistic information (semantic, grammatical) about the word and it's relationship to other words. This is fed into the classifier and improves the classifier model and its ability to generalize.
