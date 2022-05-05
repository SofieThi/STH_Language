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
```output``` | the results of inputting the network_data datasets


## Contribution

Sofie Thinggaard au613703

201909063@post.au.dk

## Methods

This problem relates to performing network analysis using networkx. In order to address this problem, we start by finding all the .csv files in the folder and defining the place we want our networks to be saved (outpath). Then we either select "a single file AND its extension" or we select "all". 

If a specific file is selected the following should occur: it prints the name of the file to the terminal, makes network from the read dataframe, saves file as a .png in outpath, resets graph so it doesn't write on top of each other, print to terminal: "A graph of the calculated network has been saved as a png in the output folder". Furthermore, we generate a .csv with eigenvector centrality measures, betweenness centrality measures, degree centrality and rename the column names to match (we have to join the dataframes in stages). This is saved with the outpath and name of the csv based on the data file's name. 

If "all", on the other hand, is selected the same should occur but for ALL the .csv files.

-If the file is found the following will show: "A csv file containing calculated betweenness centrality, eigenvector centrality and degree centrality has been saved in the Output folder"

-If no file is found the following will show: "the file could not be found - Please be sure to enter the corrent filename AND file extension (eg. '.csv')"


## Usage (reproducing results)

To run this code, when asked the name of the file to perform network analysis on, input either a single file's name + file extension (eg. '.csv') or input all to do network analysis on all the files. 

To replicate the results chose the files in the folder called network_data

#### Important
No quotes or space when asked the name of the file to perform network analysis on


## Discussion of results

Results: getting a .csv file that shows name; degree centrality; betweenness centrality; eigenvector centrality of either a single file or all in the folder. Furthermore, a visualization of the network, also for a single file or all in the folder.
