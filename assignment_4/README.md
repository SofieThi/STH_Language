## Assignment 4 - Text classification

The two scripts do the following:

-->The first script should perform benchmark classification using standard machine learning approaches

This means CountVectorizer() or TfidfVectorizer(), LogisticRegression classifier

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

This problem relates to text classification. We are going to train a model to predict whether or not a comment is toxic or non-toxic. The first script: assign_lr.py performs benchmark classification using standard machine learning approaches (TfidfVectorizer(), LogisticRegression classifier). Firstly, we create more balanced dataset by getting a random sample of the dataset (1000 datapoints), then we create new variables called text and label, then we do a train-test split, create vectorizer object using TfidfVectorizer, this vectorizer is then used to turn all of our documents into a vector of numbers, instead of text, then we classify and predict with LogisticRegression. We make a classification report and save it to an output folder. 

The second script: assign.dl.py performs classification using deep learning methods with Keras Embedding layer, Convolutional Neural Network. Firstly, we create new variables called text and label, do a train-test split, clean and normalize data (lots of noise like html tags), then we define what to do if model encounter unknown words it has not seen during training= UNK, we fit tokenizer on the documents, we set a padding value (because we have different lengths of documents, so need a max doument length. If shorter= padding of zeros), we then tokenize all documents using this fit tokenizer, we do a sequence normalization (sequence= anything that can be iterated over), we add padding to sequences, we encode labels, we define parameters for the model and create it and train it. Finally, we can evaluate and make a classification report and save to an output folder.

## Usage (reproducing results)

In order to run this code, clone the repository and store the data in the data folder. You will need the packages in the requirements.txt document.

To replicate the results chose the dataset VideoCommentsThreatCorpus.csv

## Discussion of results

Results: The first script with the LogisticRegression classifier (assign_lr.py) had an accuracy of 72% 

The second script with the classification using deep learning methods (assign_dl.py) had an accuracy score of 97% 
