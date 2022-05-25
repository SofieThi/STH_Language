## Assignment 1 - Collocation tool

The script does the following:

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
```output``` | the results of inputting the text: Bennet_Helen_1910.txt and search_term "park"

## Contribution

Sofie Thinggaard au613703

201909063@post.au.dk

## Methods

This problem relates to finding how often words appear together in a given window size (collocation). In order to address this problem, we first chose a text (the default: Bennet_Helen_1910.txt) and make it all lower case and tokenize the text. Then we define a search term (can chose from the terminal) and a window size (default: ± 5). 
First, we count how many instances of the search_term (I chose "park") occur in the chosen text. Next, we get the index of context words in the window (without counting the search term) and then get the words themselves that match the index. 
We then get the mutual information (MI) score by using this formula: MI = log ( (AB * sizeCorpus) / (A * B * span) ) / log (2) from https://www.english-corpora.org/mutualInformation.asp We now need to find all the variables:

First, we need to find A: the frequency of node word

Second, we need to find B: the frequency of collocate

Third, we need to find AB: the frequency of collocate near the node word

Fouth, we need to find size of the corpus (the text)

Fifth, we need to find the span of words

MI can then be calculated

We get the 'words', 'B', 'AB', 'MI' into a dataframe and make it into a .csv

## Usage (reproducing results)

In order to run this code, clone the repository and store the data in the data folder. The data is from Github: https://github.com/computationalstylistics/100_english_novels. You will need the packages in the requirements.txt document. 

Input the desired search term when asked "what is your search term?" in the terminal. You can also change the window size (± 5 in this code) and the text manually, by changing the range and the filepath.

To replicate the results chose the text Bennet_Helen_1910.txt and set the search_term to "park" (no quotation marks or uppercase when chosing search word).

## Discussion of results

Results: getting a .csv file with all the words within a specific window size to a search term ordered into the columns: the collocate term (words), how often it appears in the text (B), how often it appears as a collocate (AB) and the mutual information score (MI). The word "park" is strongly associated with words like "equals", "splendours", "mentions", "vaunted", and "benches".

One problem with this method is that it also counts stop words like "the" and "a" and punctuation, and they are prominent in the output data. These are rarely relevant for analysis and could be removed.

## Link to assignment 1 on Github

https://github.com/SofieThi/STH_Language/tree/main/assignment_1
