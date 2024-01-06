# Word Transformation Graph
Author

    Name: Soumya Dayal
    Username: sd9829

# Overview
This Python script provides a word transformation path from a given starting word to an ending word using a graph-based approach. The words in the input file are considered as nodes, and two nodes are connected if they can be transformed into each other by changing a single letter. The script performs a BFS traversal on a word graph, looking for a sequence of word transformations from a starting word to an ending word, where each transformation involves replacing a single character with '*'

# How to Use
Create a file with a list of words. For example, create a file named "exampleWords" and add the following 10 words to it:

short
shirt
share
shark
sharp
shaft
shift
swift
drift
drain

Save the file.

Run the Python script by executing it in the terminal:

bash: python word_transform.py
The script will execute with default arguments: begin_word="short" and end_word="abort".
The script will print the word transformation path from the specified starting word to the ending word if it exists. If not, it will print "No solution."

# Example

Suppose we have the following 10 words in the "exampleWords" file:

short
shirt
share
shark
sharp
shaft
shift
swift
drift
drain

Running the script with default arguments might produce the following output:

short
shirt
shift
swift

This indicates a word transformation path from "short" to "abort."

Feel free to modify the "exampleWords" file and the arguments in the main function of the script to test different word transformation scenarios.
