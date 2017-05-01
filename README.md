# Corpus Consistency

## Description of the inner workings
Count the occurrences of a word or multiple words that form a topic per document in the corpus.
For continuity and consistency research, this corpus can be ordered chronologically.
The sample size and size of the sample window (amount of words within which to count the words of interest) are calculated for a given statistical confidence level.
Statistics of choice are then plotted to visualise the word occurrences.

## Adding a corpus
For the most basic use, put a `corpus` folder in the folder that contains `corpus_consistency.py`.
Otherwise place a folder in `path/to/corpus` and provide this in the path specification via the command line tool.

The corpus must consist of only `.txt` files.
Each file will be seen as a distinct document and all statistics are calculated within documents.

## Using the tool via the command line
For help on using the program, use:

`python corpus_consistency.py -h`

To search for `word1`, use:

`python corpus_consistency.py word1`

Or to search for a whole topic [word1, word2, word3], use:

`python corpus_consistency.py word1 word2 word3`

Optional arguments are corpus path specification:

`python corpus_consistency.py --path path/to/corpus word1`

Or confidence level selection, as a percentage between 0.0 and 1.0:

`python corpus_consistency.py --confidence 0.95 word1`

Or statistical function plot type, selected from one of the available types [`standard_deviation`, `box_plot`]:

`python corpus_consistency.py --functionType standard_deviation word1`
