# cosmic-sorter
This program can filter COSMIC's Mutation Data and Gene Expression Data via RegEx strings in O(n) time

# setup.py

First split each of the datafiles into 3242 expression files, and 176 mutation files. Place the mutation files at the in a folder named "Cases" and the Expression files in a folder named "Expression"  run this program in the directory containing both of these folders.

As long as you dont change directories, you do not need to repeat this step.

# betterSorter.py
Name is temporary
betterSorter.py reads request.txt, then searches all the data setup by setup.py and returns a list of all TCGA-IDs of patients who meet the criteria in request.txt


