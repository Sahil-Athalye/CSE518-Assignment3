#!/usr/bin/env python3

import os

# Define input and output directories
input_folder = "/Users/sahil/Documents/Human-in-the-Loop Computation/Assignment 3/Random Lists"
output_folder = "/Users/sahil/Documents/Human-in-the-Loop Computation/Assignment 3/Truth Lists"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def read_word_list(filepath):
    """
    Reads a text file where each line contains one word.
    Returns a list of words.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        # Remove any blank lines
        words = [line.strip() for line in f if line.strip()]
    return words

def write_word_list(filepath, word_list):
    """
    Writes the word list to the specified file, one word per line.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        for word in word_list:
            f.write(word + "\n")

def sort_file_alphabetically(input_path, output_path):
    """
    Reads the word list from input_path, sorts it alphabetically,
    and writes the sorted list to output_path.
    """
    words = read_word_list(input_path)
    # Sort words in a case-insensitive manner
    sorted_words = sorted(words, key=str.lower)
    write_word_list(output_path, sorted_words)
    print(f"Processed file: {os.path.basename(input_path)}")

def main():
    # Process each text file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename)
            sort_file_alphabetically(input_file, output_file)

if __name__ == "__main__":
    main()