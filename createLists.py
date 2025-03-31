import random
import os
from nltk.corpus import words 
import nltk
import openai
import time

    
nltk.download('words')
word_list = words.words()


# Function to generate a shuffled word list of given size
def generate_shuffled_list(size):
    return random.sample(word_list, size)

# Creating lists
sizes = [20, 20, 20, 20]
lists = []
for i in range(len(sizes)):
    size = sizes[i]
    shuffled_list = generate_shuffled_list(size)
    lists.append(shuffled_list)

def to_lowercase_nested(lists):
    return [[word.lower() for word in sublist] for sublist in lists]

lowercase_lists = to_lowercase_nested(lists)

# Create output directory
# output_dir = "Random Lists"
# os.makedirs(output_dir, exist_ok=True)

# Save each list to a separate text file
# for i in range(len(lowercase_lists)):
#     size = sizes[i]
#     words = lowercase_lists[i]
#     filename = os.path.join(output_dir, f"{i}.txt")
#     with open(filename, "w") as f:
#         f.write("\n".join(words))

