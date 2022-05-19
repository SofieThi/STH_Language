# Data analysis
import os
import pandas as pd
from tqdm import tqdm #quick overview of time (progress bar)

# NLP
import spacy
nlp = spacy.load("en_core_web_sm") #English model

# sentiment analysis VADER
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer() #using VADER for the analysis

# visualisations
import matplotlib.pyplot as plt #simple visulizations

#Making a list of all sentiment scores for every headline (aka the title column) in the dataset
#No function inside a function
def sent_score(dataframe_column):
    output_list =[] #empty list for inputting the sentiment score
    for title in dataframe_column: #For every single title in the "title" column in the pandas dataframe
        score = analyzer.polarity_scores(title) #score using VADER
        output_list.append(score) #appending to the list
    return output_list

def main():
    # Load the data:
    # get the filepath
    filepath = os.path.join("..","..","CDS-LANG","tabular_examples","fake_or_real_news.csv")
    
    # load the data
    #open csv with pandas
    data = pd.read_csv(filepath)
    
    #looking at the dataset
    print(data)
    
    #Getting textID
    #Rename column 0 (the unnamed column) textID.
    data.rename(columns={'Unnamed: 0':'textID'}, inplace=True)
    print(data)
    
    #Getting sentiment score for a single text in the dataset
    text_example = data["title"] [3] #Getting the 4th file in the dataset
    print(text_example)
    
    analyzer.polarity_scores(text_example)
    #slightly negative
    
    # use my sent_score function (Making a list of all sentiment scores for every headline)
    sentiment_score = sent_score(data["title"])
    
    print(sentiment_score)
    
    #Getting the sentiment score for every headline in the dataset into a dataframe
    sentiment_df = pd.DataFrame(sentiment_score, columns= ["neg", "neu", "pos", "compound"]) #columns
    print(sentiment_df)
    
    #combining the two dataframes: 'data' dataframe and 'sentiment_df' dataframe
    sentimentedDF = pd.concat([data, sentiment_df], axis=1, join='inner')
    print(sentimentedDF)
    
    #Finding mentions of geopolitical entites in headlines (aka title column)
    #two empty lists
    ents = []
    headline_title = []

    for headline in tqdm(nlp.pipe(data["title"], batch_size=500)): #tqdm = progress bar #formula from session_5
        for entity in headline.ents:
            #only keep entities if they are GPE (geopolitical entities)
            if entity.label_ == "GPE":
                headline_title.append(headline.text) #headline text into headline_title list
                ents.append(entity.text) #GPE into the ents list
            else:
                continue
                
    print(len(ents)) #Checking if the two lists are the same length
    print(len(headline_title))
    
    # getting the two lists in a combined dataframe
    GPE_test = pd.DataFrame({"title": headline_title, "GPE Found": ents})
    GPE_test.head(20) #Getting the first 20 entries in the dataset (there are many)
    
    #combining the previously combined dataframe (the one with sentiments) and the new dataframe (the one with GPEs)
    mergedDF = pd.merge(sentimentedDF, GPE_test, on="title", how = "outer") 
    #you apprently need an outer-join in order to get the texts where no GPEs are found (NaN = Not a number)
    #inner-joining will result in getting only entries where a GPE has been found in the title
    print(mergedDF)
    
    #Now splitting the dataset: splitting into real news
    real_news = mergedDF[mergedDF['label'] == "REAL"]
    print(real_news)
    
    #Counting the GPE's in the real_news dataset
    real_news.value_counts("GPE Found")
    
    #Plotting the 20 most frequently mentioned GPE in the real news dataframe as a Bar Chart
    AxesSubplot = real_news['GPE Found'].value_counts().nlargest(20).plot.bar()
    
    #save the 20 most frequently mentioned GPE in the real news subset in output folder
    AxesSubplot.get_figure().savefig(os.path.join("output/real_bar_chart.png"))
    
    print("Done! bar chart has been generated and saved in the output folder as real_bar_chart.png")
    
    #doing the same with the fake news category
    #Splitting the data into fake_news
    fake_news = mergedDF[mergedDF['label'] == "FAKE"] 
    print(fake_news)
    
    #Counting the GPEs in the fake_news dataset
    fake_news.value_counts("GPE Found")
    
    #Plotting the 20 most frequently mentioned GPE in the fake news dataframe as a Bar Chart
    AxesSubplot_2 = fake_news['GPE Found'].value_counts().nlargest(20).plot.bar()
    
    #save the 20 most frequently mentioned GPE in the fake news subset in output folder
    AxesSubplot_2.get_figure().savefig(os.path.join("output/fake_bar_chart.png"))
    
    print("Done! bar chart has been generated and saved in the output folder as fake_bar_chart.png")
    
    #saving the dframe in specific folder
    mergedDF.to_csv(os.path.join("..","..","cds-lang", "Lang-assignments", "output", "df_assign_2.csv"))

    print("Done! dframe has been generated and saved in the output folder as assign_2.csv")
    
                    
if __name__=="__main__":
    main()