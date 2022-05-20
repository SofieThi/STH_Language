# simple text processing tools
import os
import re
import tqdm
import unicodedata
import contractions
from bs4 import BeautifulSoup #remove things that are non-text
import nltk #we used spacy in the past
nltk.download('punkt')

# data wranling
import pandas as pd
import numpy as np

# tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (Dense, 
                                    Flatten,
                                    Conv1D, 
                                    MaxPooling1D, 
                                    Embedding)
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence

# scikit-learn
from sklearn.metrics import (confusion_matrix, 
                            classification_report)
from sklearn.preprocessing import LabelBinarizer, LabelEncoder

# Machine learning stuff
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier 
from sklearn.model_selection import ShuffleSplit
from sklearn import metrics

# visualisations 
import matplotlib.pyplot as plt
# %matplotlib inline #wont work


# fix random seed for reproducibility
seed = 42
np.random.seed(seed)

#Helper functions for text processing
def strip_html_tags(text):
  soup = BeautifulSoup(text, "html.parser")
  [s.extract() for s in soup(['iframe', 'script'])]
  stripped_text = soup.get_text()
  stripped_text = re.sub(r'[\r|\n|\r\n]+', '\n', stripped_text)
  return stripped_text

def remove_accented_chars(text):
  text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
  return text #everything is in English: no accented characters in English. When used here, it could be used incorrectly/inconsistently

def pre_process_corpus(docs):
  norm_docs = []
  for doc in tqdm.tqdm(docs):
    doc = strip_html_tags(doc)
    doc = doc.translate(doc.maketrans("\n\t\r", "   "))
    doc = doc.lower() #lower case
    doc = remove_accented_chars(doc) #no accented characters
    doc = contractions.fix(doc) #resolves contractions: you're -> you are
    # lower case and remove special characters\whitespaces
    doc = re.sub(r'[^a-zA-Z0-9\s]', '', doc, re.I|re.A)
    doc = re.sub(' +', ' ', doc)
    doc = doc.strip()  
    norm_docs.append(doc)
  
  return norm_docs


def main():  
    # Load the data:
    # get the filepath
    filepath = os.path.join("data")

    #open csv with pandas
    data = pd.read_csv(filepath)

    #looking at the dataset
    print(data)

    # create new variables called text and label
    # taking the data out of the dataframe so that we can mess around with them.
    X = data["text"] #text column
    y = data["label"] #label column

    #Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, #texts for the model
                                                        y, #classification labels
                                                        test_size = 0.2, #create an 80/20 split (testing to be 20% of the overall data)
                                                        random_state = 42) #where we should start: just for reproducability

    #clean and normalize data (lots of noise like html tags) see helper cell
    X_train_norm = pre_process_corpus(X_train)
    X_test_norm = pre_process_corpus(X_test)

    #looking at the first comment
    print(X_train_norm[0]) #the first one

    #Tokenize sequences
    # creates index of every word in doc, converts all word to number in index in training data

    #define out-of-vocabulary-token
    t = Tokenizer(oov_token = "<UNK>")
    #model has not encountered during training= unknown

    #fit the tokenizer on the documents
    t.fit_on_texts(X_train_norm)

    #set padding value (different lengths of documents etc. need a max doument length. If shorter= padding of zeros)
    t.word_index["<PAD>"] = 0


    #tokenize all documents using this fit tokenizer
    #sequence: anything that can be iterated over
    X_train_seqs = t.texts_to_sequences(X_train_norm)
    X_test_seqs = t.texts_to_sequences(X_test_norm)

    #Sequence normalization
    MAX_SEQUENCE_LENGTH = 1000

    #add padding to sequences
    X_train_pad = sequence.pad_sequences(X_train_seqs, maxlen= MAX_SEQUENCE_LENGTH)
    X_test_pad = sequence.pad_sequences(X_test_seqs, maxlen= MAX_SEQUENCE_LENGTH)

    #checking everything is working
    X_train_pad.shape, X_test_pad.shape #22914 or 5729 comments that are all 1000 tokens long

    #label encoder
    le = LabelEncoder()
    num_classes = 2 #toxic -> 1, non-toxic -> 0
    y_train_le = le.fit_transform(y_train)
    y_test_le = le.transform(y_test)

    #Create and compile model

    #define parameters for model
    #overall vocabulary size
    VOCAB_SIZE = len(t.word_index)
    #number of dimensions for embeddings
    EMBED_SIZE = 300
    #number of epochs to train for
    EPOCHS = 2
    #batch size for training
    BATCH_SIZE = 128

    # create the model
    model = Sequential()
    # embedding layer NEW LAYER!
    model.add(Embedding(VOCAB_SIZE, #vocabulary of certain size
                        EMBED_SIZE, #number of dimensions for embeddings
                        input_length=MAX_SEQUENCE_LENGTH)) #1000 characters

    # first convolution layer and pooling
    model.add(Conv1D(filters=128, #128 different kernels, 128 times learning
                            kernel_size=4, 
                            padding='same',
                            activation='relu'))
    model.add(MaxPooling1D(pool_size=2)) #max pooling= biggest value is the one being predicted

    # second convolution layer and pooling
    model.add(Conv1D(filters=64, #64 kernels, half of before
                            kernel_size=4, 
                            padding='same', 
                            activation='relu'))
    model.add(MaxPooling1D(pool_size=2))

    # third convolution layer and pooling
    model.add(Conv1D(filters=32, #32 kernels, half of before
                            kernel_size=4, 
                            padding='same', 
                            activation='relu'))
    model.add(MaxPooling1D(pool_size=2))

    # fully-connected classification layer
    model.add(Flatten()) #one vector for each document
    model.add(Dense(256, activation='relu'))
    model.add(Dense(1, activation='sigmoid')) #only one node is wanted in output
    model.compile(loss='binary_crossentropy', #sentiments: positive/negative= binary prediction: true/false
                            optimizer='adam', #not sgd
                            metrics=['accuracy'])
    # print model summary
    print(model.summary())

    #train
    history = model.fit(X_train_pad, y_train_le,
                        epochs = EPOCHS,
                        batch_size = BATCH_SIZE,
                        validation_split = 0.1, #usually only test/training split, but now training is getting split further
                        verbose = True) #gives updates on screen while training
    #verbose = 0: nothing, 1: progress that updates all the time

    #evaluate the model
    scores = model.evaluate(X_test_pad, y_test_le, verbose=1)
    print(f"Accuracy: {scores[1]}")

    #loss value and accuracy
    print(scores)

    model.predict(X_test_pad)

    # 0.5 decision boundary
    predictions = (model.predict(X_test_pad) > 0.5).astype("int32")
    # assign labels
    predictions = ["toxic" if item == 1 else "non-toxic" for item in predictions]
    y_test = ["toxic" if item == 1 else "non-toxic" for item in y_test]
    print(predictions[:20]) #20 first predictions

    #confusion matrix and classification report
    labels = ["non-toxic", "toxic"]
    print(classification_report(y_test, predictions))
    pd.DataFrame(confusion_matrix(y_test, predictions), 
                 index=labels, columns=labels)

    report = classification_report(y_test, predictions, target_names = labels)

    f = open("output/deep_learning_assign_4.txt",'w') #saving in this folder as assign_4.1.txt
    print(report, file=f)

    print("Done! Report has been generated and saved in the output folder as deep_learning_assign_4.txt")


if __name__=="__main__":
    main()