# import package and initialize it
import spacy

# creating NLP pipeline
nlp = spacy.load("en_core_web_sm")

#others
import os
import math
import pandas as pd

def main():
    # create spacy doc from one of the novels in the shared data folder
    # import and open the novel
    filepath = os.path.join("..", "..", "CDS-LANG", "100_english_novels", "corpus", "Bennet_Helen_1910.txt")

    file_object = open(filepath, "r")
    doc = file_object.read()

    # making whole novel lower case text
    doc = doc.lower()
    # tokenizes
    doc = nlp(doc)
    
    # Defining a search term
    # User-defined search term is currently: park
    search_term = input("what is your search term?") #insert search term
    
    # counting how many instances of search_term park
    counter = 0    
    for token in doc:
        if token.text == search_term: #If it is the search_term:
            counter += 1 #add one
    
    # printing in a sentence how many times search_term (park) is in the text
    print("There are " + str(counter) + " instances of " + search_term + " in the text")
    
    #getting index of context words
    index = []

    for token in doc:
        if token.text == search_term: #If it is the search_term:
            before = token.i - 5 #5 words before search_term
            for i in range(before, before + 10):
                if i != token.i: #not-equal-to
                    index.append(i)
    print(index)
    
    #getting the context words - the words that match the index
    words = []

    for token in doc:
        if token.text == search_term: #If it is the search_term:
            #get the index
            # get the start of the preceding context
            before = token.i -5 #window size before word
            # get the end of the following context
            after = token.i +5 #window size after word
            for i in range(before, after):
                if str(doc[i]) != search_term:
                    words.append(doc[i])
    print(words)  
    
    
    # calculating mutual information score for one of the context words: 
    # formula from https://www.english-corpora.org/mutualInformation.asp
    
    # The formula: MI = log ( (AB * sizeCorpus) / (A * B * span) ) / log (2)
    # need to find all the variables

    #A = frequency of node word: 
    counter = 0    
    for token in doc:
        if token.text == search_term:
            counter += 1
    A = counter #defining A as 
    print("The word >" + search_term + "< is mentioned " + str(A) + " times")
    
    #B = frequency of collocate
    B = [] #empty list
    for i in range(0, len(words)-1): 
        B_words = str(words[i]) 
        counter2 = 0 
        for token in doc:
            if token.text == B_words: #if it finds B_words
                counter2 += 1 #add 1
        B.append(counter2) #adding to freqency to the list
    
    #AB = frequency of collocate near the node word
    AB = [] #empty list
    for i in range(0, len(words)-1): 
        B_words = str(words[i])
        counter3 = 0 
        for token in words:
            if token.text == B_words:
                counter3 += 1
        AB.append(counter3) #appending to the list

    print("Number of times the 5th word before the search_term >" + B_words + "< is mentioned " + str(counter3) + " within in the 10 words close to >" + search_term + "<")
    
    #sizeCorpus= size of corpus
    sizeCorpus = textLength = len(token.doc)
    print(textLength)
    
    #span = span of words
    span = 10
    #log (2) is literally the log10 of the number 2: .30103
    math.log(2,10)

    #MI = 11.37 = log ( (24 * 96,263,399) / (1262 * 115 * 6) ) / .30103

    MI = []
    for i in range(0, len(words)-1): 
        MI1 = math.log((AB[i]*sizeCorpus)/(A*B[i]*span))/math.log(2,10)
        MI.append(MI1)
        
        print(MI)
        
    #Combine context words to the search term and their scores
    list_context=list(zip(words, B, AB, MI))
    # Converting lists of tuples into pandas Dataframe.  
    dframe = pd.DataFrame(list_context, columns=['words', 'B', 'AB', 'MI'])  
    # Print data
    print(dframe)
    
    #saving the dframe in specific folder
    dframe.to_csv(os.path.join("..","..","cds-lang", "Lang-assignments", "output", "assign_1.csv"))
    
print("Done! dframe has been generated and saved in the output folder as assign_1.csv")
    
if __name__=="__main__":
    main()