## Assignment 3 - Network analysis

The script does the following:

-If the user enters a single filename as an argument on the command line:

Load that edgelist

Perform network analysis using networkx

Save a simple visualisation

Save a CSV which shows the following for every node:
name; degree; betweenness centrality; eigenvector_centrality

-If the user enters a directory name as an argument on the command line:

Do all of the above steps for every edgelist in the directory

Save a separate visualisation and CSV for each file



## Structure

This repository has the following directory structure:

| Column | Description|
|--------|:-----------|
```data```| a folder to be used for inputting the data you wish to run
```notebooks``` | Jupyter notebooks in both .ipynb and .html format
```src``` | the .py script version of the assignment
```output``` | the results of inputting the network_data's cvs files


## Contribution

Sofie Thinggaard au613703

201909063@post.au.dk

## Methods

This problem relates to performing network analysis using networkx. The network consists of nodes (the objects we are studying, here characters in books) and edges (the relationship between the characters in the books). In order to address this problem, we start by finding all the .csv files in the folder and defining the place we want our networks to be saved (outpath). From the command line, chose either "a single file AND its extension" or select "All". 

If a specific csv file from the folder is selected the following should occur: it prints the name of the file to the terminal, makes network from the read dataframe, saves file as a .png in outpath, resets graph so it doesn't write on top of each other, print to terminal: "A graph of the calculated network has been saved as a png in the output folder". Furthermore, we generate a .csv with eigenvector centrality measures, betweenness centrality measures, degree centrality and rename the column names to match (we have to join the dataframes in stages). This is saved with the outpath with name of the csv based on the data file's original name. 

If All, on the other hand, is selected the same should occur but for ALL the defined .csv files.

-If the input in the terminal is written correctly, the following will show: "A csv file containing calculated betweenness centrality, eigenvector centrality and degree centrality has been saved in the Output folder"

-If something went wrong and no file is found the following will show: "the file could not be found - Please be sure to enter the corrent filename AND file extension (eg. '.csv')"

## Usage (reproducing results)

In order to run this code, clone the repository and store the data in the data folder. The data is from the network_data folder. You will need the packages in the requirements.txt document.

When asked the name of the file to perform network analysis on, input either a single file's name + file extension (eg. '.csv') or input "all" to do network analysis on all the files. 

To replicate the results chose the files in the folder called network_data

#### Important

No quotatition marks or space when asked the name of the file to perform network analysis on. Capitalization also matters!

## Discussion of results

Results: getting information about specific book's relationship between characters. If you have a problem with objects connected in some kind of way, network analysis can be utilzed to study it, as is the case with these books in the dataset. The output data can be used for an analysis of a specific book's internal structure and could possibly be compared to other works in the period or from the same author. 

Using this code gets you a .csv file that shows name; degree centrality; betweenness centrality; eigenvector centrality of either a single file or of all the .csvs in the folder. Node centrality metrics include degree centrality (the number of edges connected to a node), eigenvector centraility (how well-connected a node is to other well connected nodes) and betweeness centrality (nodes located on the communication path to important nodes - connects other nodes) Furthermore, a visualization of the network for a single file or for all in the folder is generated.
