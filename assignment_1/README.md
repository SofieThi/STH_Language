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
