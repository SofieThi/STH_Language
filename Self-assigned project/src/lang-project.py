# data processing tools
import os
import csv
import urllib.request
import pandas as pd
from tqdm import tqdm

# Huggingface tools
from transformers import AutoTokenizer
from transformers import TFAutoModelForSequenceClassification #sequence classification
from transformers import pipeline, set_seed

#classification report
from sklearn.metrics import (confusion_matrix, 
                            classification_report)

def main():
    #which model do we want to use?
    MODEL = f"siebert/sentiment-roberta-large-english" #URL
    
    #initalize a pretrained tokenizer (to tokenize the texts)
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    
    #Initialize the model
    model = TFAutoModelForSequenceClassification.from_pretrained(MODEL) 
    #pytorch = tensorflow is what we use, so we need to use TF at start, see start
    
    #load the data from https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
    filename = os.path.join("data")
    data = pd.read_csv(filename)

    print(data)
    
    #converting negative and positive into ones and zeros to match the model
    data['sentiment'] = data['sentiment'].map({'negative': 0, 'positive': 1})
    
    print(data)
    
    #making the very large dataset smaller: make a subset of 500 reviews
    data = data.head(500)
    
    print(data)
    
    #making a pipeline to quickly generate results with default parameters
    sentiment_analysis = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english")
    
    #some of the reviews are too long for the model to do sentiment analysis on
    #so we make a list of those reviews it is able to score and another list with the reviews that are too long

    sentiment_scores = [] #list for reviews for the model to do sentiment analysis on
    bad_ids = [] #list for reviews that are too long to do sentiment analysis on
    #for every row in my data
    for idx, row in tqdm(data.iterrows()):
        #iterate over pandas dataframe (go through all entrys in df)
        #make prediction on the review column
        try:
            # try the following code to extract sentiment
            predictions = sentiment_analysis(row["review"])
            #append to the empty output list called sentiment_scores
            sentiment_scores.append(predictions)
        except:
            # if that doesn't work, just print this and move on:
            print(f"Oops! Review {idx} is too long for the model!")
            # a list of ids to be excluded: append to the bad_ids list
            bad_ids.append(idx)
    
    #look at the scored reviews
    print(sentiment_scores)
    
    #look at the non-scored reviews (those that are too long)
    print(bad_ids)
    
    #make list keeping only the prediction (not certainty)
    predicted_labels = []
    for score in sentiment_scores:
        label = score[0]["label"]
        predicted_labels.append(label.lower()) #lowercase the predictions to match the IMDB labels
    
    #we are left with the prediction in lower case
    print(predicted_labels)
    
    #keep only the scored labels in list in our data
    scores_keep = []
    for idx, row in data.iterrows():
        # if row index is in the bad_id list (too long)
        if idx in bad_ids:
            # do nothing
            pass
        else:
            # if its not in the bad_id list then keep the score
            scores_keep.append(row)
            
    # keep only the data we want into a df
    keep_data = pd.DataFrame(scores_keep)
    
    print(keep_data)
    
    #classification report to get an overview of how well the model is performing
    scores_keep = ["positive" if item == 1 else "negative" for item in keep_data["sentiment"]]
    
    labels = ["negative", "positive"]
    print(classification_report(scores_keep, predicted_labels))
    
    #save the model in output folder
    report = classification_report(scores_keep, predicted_labels, target_names = labels)

    f = open("output/project_classification.txt",'w') #saving in this folder as project_classification.txt
    print(report, file=f)

    print("Done! Report has been generated and saved in the output folder as project_classification.txt")
    
    #is the model better at predicting negative or positive sentiments?
    cm = pd.DataFrame(confusion_matrix(scores_keep, predicted_labels), 
                 index=labels, columns=labels)
    
    print(cm)
    
    #save the matrix to output folder
    cm.to_csv("output/confusion_matrix.csv")

    print("Done! Confusion matrix has been generated and saved in the output folder as confusion_matrix.csv")
    
if __name__=="__main__":
    main()
