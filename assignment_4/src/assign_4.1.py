#to train a Logistic Regression model using scikit-learn, from vis_assign_2

#session_8
# system tools
import os
import sys
sys.path.append(os.path.join("..", "..", "CDS-LANG"))

# data munging tools
import pandas as pd
import utils.classifier_utils as clf

# Machine learning stuff
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier 
from sklearn.model_selection import ShuffleSplit
from sklearn import metrics

# Visualisation
import matplotlib.pyplot as plt
import seaborn as sns

#surpress warnings
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
    os.environ["PYTHONWARNINGS"] = "ignore" #ignore warnings
    
#scikit-learn
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report

# data wranling
import numpy as np

import os

def main():
    # Load the data:
    # get the filepath for test labels
    filepath = os.path.join("..","..","CDS-LANG","toxic","VideoCommentsThreatCorpus.csv")    

    #open csv with pandas
    data = pd.read_csv(filepath)

    #looking at the dataset
    print(data)
    #1 = toxic, 0= non-toxic

    #create more balanced dataset, getting a random sample of the dataset
    data_balanced = clf.balance(data, 1000) #1000 datapoints for each    

    # create new variables called text and label
    # taking the data out of the dataframe so that we can mess around with them.
    X = data_balanced["text"] #text column
    y = data_balanced["label"] #label column    

    #Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, #texts for the model
                                                        y, #classification labels
                                                        test_size = 0.2, #create an 80/20 split (testing to be 20% of the overall data)
                                                        random_state = 42) #where we should start: just for reproducability

    # Create vectorizer object
    #can modify all of these parameters (or not set any)
    vectorizer = TfidfVectorizer(ngram_range = (1,2), #the size of tokens: unigrams and bigrams (1: individual words and 2 word pairings: repeated word pattern)
                                 lowercase = True, #use lowercase: getting all instances of the word
                                 max_df = 0.95, #remove very common words, stop words, if these words appear in over 95% of the documents= gone
                                 min_df = 0.05, #remove very rare words, occur in fewer than 0.05% of the documents= gone, does not "discriminate"
                                 max_features = 100) #keep only top 500 features (compress to focus on the 500 most frequent words- further filtering)   

    #This vectorizer is then used to turn all of our documents into a vector of numbers, instead of text.
    #use on all documents
    #first we fit to the training data
    X_train_feats = vectorizer.fit_transform(X_train)

    #we then do it for our test data
    X_test_feats = vectorizer.transform(X_test) #no fitting!! as we are trying to predict

    #get feature names: the unigrams and bigrams
    feature_names = vectorizer.get_feature_names()

    #Classifying and predicting
    classifier = LogisticRegression(random_state=42).fit(X_train_feats, y_train)

    #use the classifier to make predictions
    y_pred = classifier.predict(X_test_feats)

    # Evaluate
    classifier_metrics = metrics.classification_report(y_test, y_pred)
    print(classifier_metrics)

    #Save the results from the classification report to a text file
    g = open("../../cds-lang/Lang-assignments/output/benchmark_assign_4.txt",'w')
    print(classifier_metrics, file=g)

    print("Done! classifier_metrics has been generated and saved in the output folder as benchmark_assign_4.txt")
    
if __name__=="__main__":
    main()