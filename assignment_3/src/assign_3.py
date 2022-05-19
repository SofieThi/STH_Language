#importing all of the libaries and functions we'll need

# System tools
import os

# Data analysis
import pandas as pd
from collections import Counter
from itertools import combinations 
from tqdm import tqdm #progress bar

# NLP
import spacy
nlp = spacy.load("en_core_web_sm")

# Network analysis tools
import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,20)

def main():
    print("The input folder contains the following data files:")
    path = os.path.join("data") # path to input data
    filenames = os.listdir(path)
    for file in filenames: #It finds all filenames inside network_data
        filepath = os.path.join(path)
        if file.endswith(".csv"):
            print(file)

    # make path to output data
    outpath = os.path.join("output")

    # select a file
    selected_file = input("Please write the name of the file to perform network analysis on - Be sure to include file extension (eg. '.csv')")

    #Reads the csv file chosen by the user - If the user inputs a valid file name
    if selected_file == "All": #if user writes "All" above it does the following:
        for csv_file in os.listdir(path): #For all csv-files in this folder, do:
            #print(csv_file) #Test if the loop reaches all files in the folder
            if csv_file.endswith(".csv"): #only if the file is a csv file
                data = pd.read_csv(path + "/" + str(csv_file), sep='\t+', engine='python') #reads file
                print("The file: " + csv_file + " has been read. Making network graph...") #Prints the name of the read file
                G = nx.from_pandas_edgelist(data, "Source", "Target", ["Weight"]) #Makes network from the dataframe
                nx.draw_networkx(G, with_labels=True, node_size=20, font_size=14) #Does the network
                plt.savefig(outpath + "/" + str(csv_file) + ".png", dpi=300, bbox_inches='tight') #saves file as a .png in folder
                print("A graph of the calculated network for the file " + csv_file + " has been saved as a png in the Output folder") #Print that the file has been saved
                plt.clf() #Resets graph so it doesn't write on top of the others

                #Eigenvector Centrality measures
                ev = nx.eigenvector_centrality(G) #calculates Eigenvector centrality
                eigenvector_df = pd.DataFrame(ev.items()) #saves in new dataframe
                #Renaming the columns 0 and 1 to node and eigenvector_centrality
                eigenvector_df.rename(columns={list(eigenvector_df)[0]: 'node', list(eigenvector_df)[1] : 'eigenvector_centrality'}, inplace=True)

                #betweenness centrality measures
                bc = nx.betweenness_centrality(G) #calculates betweenness centrality
                betweenness_df = pd.DataFrame(bc.items()).sort_values(1, ascending=False) #saves in new dataframe
                #Renaming the columns 0 and 1 to node and betweenness_centrality
                betweenness_df.rename(columns={list(betweenness_df)[0]: 'node', list(betweenness_df)[1] : 'betweenness_centrality'}, inplace=True)

                #Joining the two data frames on node in order to get both eigenvector AND betweenness in one dataframe
                mergedDF = pd.merge(eigenvector_df, betweenness_df, on="node", how = "inner")

                #degree centrality
                degree = nx.degree_centrality(G) #calculates degree centrality
                degree_df = pd.DataFrame(degree.items()) #saves in new dataframe
                #Renaming the columns 0 and 1 to node and degree_centrality
                degree_df.rename(columns={list(degree_df)[0]: 'node', list(degree_df)[1] : 'degree_centrality'}, inplace=True)

                #Joining degree centrality dataframe with the eigenvector/betweenness dataframe
                mergedDF = pd.merge(mergedDF, degree_df, on="node", how = "inner")

                #Defining the path and name of the csv based on the main csv data file and outputting csv file
                csv_path = outpath + "/output_" + str(csv_file) #Output file with get a unique name based on the input file
                mergedDF.to_csv(csv_path)
                print("A csv file containing calculated betweenness centrality, eigenvector centrality and degree centrality has been saved in the Output folder")

    elif os.path.exists(path + "/" + str(selected_file)) == True: #If user on the other hand writes a specific csv file, do the following:
        data = pd.read_csv(path + "/" + str(selected_file), sep='\t+', engine='python') #Reading file
        print("The file: " + selected_file + " has been read. Making network graph...") #Prints the name of the file to the terminal
        G = nx.from_pandas_edgelist(data, "Source", "Target", ["Weight"]) #Makes network from the dataframe
        nx.draw(G, with_labels=True, node_size=20, font_size=14) #Makes the network
        plt.savefig(outpath + "/" + str(selected_file) + ".png", dpi=300, bbox_inches='tight') #saves file as a .png in folder
        plt.clf() #Resets graph so it doesn't write on top of each other
        print("A graph of the calculated network has been saved as a png in the Output folder") #for terminal

        #Eigenvector Centrality measures
        ev = nx.eigenvector_centrality(G) #calculates Eigenvector centrality
        eigenvector_df = pd.DataFrame(ev.items()) #saves in new dataframe
        #Renaming the columns 0 and 1 to node and eigenvector_centrality
        eigenvector_df.rename(columns={list(eigenvector_df)[0]: 'node', list(eigenvector_df)[1] : 'eigenvector_centrality'}, inplace=True)

        #betweenness centrality measures
        bc = nx.betweenness_centrality(G) #calculates betweenness centrality 
        betweenness_df = pd.DataFrame(bc.items()).sort_values(1, ascending=False) #saves in new dataframe
        #Renaming the columns 0 and 1 to node and betweenness_centrality
        betweenness_df.rename(columns={list(betweenness_df)[0]: 'node', list(betweenness_df)[1] : 'betweenness_centrality'}, inplace=True)

        #Joining the two data frames on node in order to get both eigenvector AND betweenness in one dataframe for easier csv export later
        mergedDF = pd.merge(eigenvector_df, betweenness_df, on="node", how = "inner")

        #Degree centrality
        degree = nx.degree_centrality(G) #calculates degree centrality
        degree_df = pd.DataFrame(degree.items()) #saves in new dataframe
        #Renaming the columns 0 and 1 to node and degree_centrality
        degree_df.rename(columns={list(degree_df)[0]: 'node', list(degree_df)[1] : 'degree_centrality'}, inplace=True)

        #Joining degree centrality dataframe with the eigenvector/betweenness dataframe
        mergedDF = pd.merge(mergedDF, degree_df, on="node", how = "inner")

        #Defining the path and name of the csv based on the main csv data file and outputting csv file
        csv_path = outpath + "/output_" + str(selected_file) #Output file with get a unique name based on the input file
        mergedDF.to_csv(csv_path) #saves as .csv
        print("A csv file containing calculated betweenness centrality, eigenvector centrality and degree centrality has been saved in the Output folder")
    else:
        print("the file could not be found - Please be sure to enter the corrent filename AND file extension (eg. '.csv')") #Error messsage if things goes wrong
    
if __name__=="__main__":
    main()
