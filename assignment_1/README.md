## Assignment 1 - Collocation tool in the course: Cultural data science

-Take a user-defined search term and a user-defined window size.

-Take one specific text which the user can define.

-Find all the context words which appear ± the window size from the search term in that text.

-Calculate the mutual information score for each context word.

-Save the results as a CSV file with (at least) the following columns: the collocate term; how often it appears as a collocate; how often it appears in the text; the mutual information score


## Structure

This repository has the following directory structure:

| Column | Description|
|--------|:-----------|
```data```| a folder to be used for inputting the data you wish to run
```notebooks``` | Jupyter notebooks in both .ipynb and .html format
```src``` | the .py script version of the assignment
```output``` | the results of inputting the dataset

## Contribution

Sofie Thinggaard au613703

201909063@post.au.dk

## Methods

This problem relates to finding how often words appear together in a given window size (collocation). In order to address this problem, we first chose a text (Bennet_Helen_1910.txt) and make it all lower case and tokenize the text. Then we define a search term (park) and a window size (± 5). 
First, we count how many instances of the search_term (park) occur in the chosen text. Next, we get the index of context words in the window (without counting the search term) and then get the words themselves that match the index. 
We then get the mutual information (MI) score by using this formula: MI = log ( (AB * sizeCorpus) / (A * B * span) ) / log (2) from https://www.english-corpora.org/mutualInformation.asp We now need to find all the variables:

First, we need to find A: the frequency of node word

Second, we need to find B: the frequency of collocate

Third, we need to find AB: the frequency of collocate near the node word

Fouth, we need to find size of the corpus (text)

Fifth, we need to find the span of words

MI can then be calculated

We get the 'words', 'B', 'AB', 'MI' into a dataframe and make it into a .csv

## Usage (reproducing results)

To run this code input your own search term when asked "what is your search term?". You can change the window size and text manually select by changing the filepath and changing the range

To replicate the results chose the text Bennet_Helen_1910.txt and set the search_term to park and the window size to ± 5

## Discussion of results

Results: getting a .csv file with all the words within a specific window size to a search term ordered into the columns: the collocate term; how often it appears as a collocate; how often it appears in the text; the mutual information score
