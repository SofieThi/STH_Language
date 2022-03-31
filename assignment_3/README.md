### Assignment 3 - Network analysis

The script does the following:

If the user enters a single filename as an argument on the command line:

Load that edgelist

Perform network analysis using networkx

Save a simple visualisation

Save a CSV which shows the following for every node:
name; degree; betweenness centrality; eigenvector_centrality

If the user enters a directory name as an argument on the command line:

Do all of the above steps for every edgelist in the directory

Save a separate visualisation and CSV for each file

### Structure
This repository has the following directory structure:

data:	a folder to be used for inputting the data you wish to run

notebooks: Jupyter notebooks in both .ipynb and .html format

src: the .py script version of the assignment

output: the results of inputting the network_data datasets

Be sure to include file extension (eg. '.csv') and no quotes or space when asked the name of the file to perform network analysis on
