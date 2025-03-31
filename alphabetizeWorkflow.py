import os
import openai
import time

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY_HERE"

# Helper function to call ChatGPT-4
def call_chatgpt(prompt, model="gpt-4", max_tokens=2000, temperature=0):
    try:
        global gpt_called
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        # print("Error calling ChatGPT:", e)
        gpt_called += 1
        print(gpt_called)
        return None

# Coarse sort: ask ChatGPT-4 to alphabetize the list
def coarse_sort(words):
    prompt = ("Please sort the following list of words into alphabetical order. "
              "Return the sorted words as a comma-separated list.\n\n"
              f"Words: {', '.join(words)}")
    sorted_response = call_chatgpt(prompt)
    if sorted_response:
        candidate = [word.strip() for word in sorted_response.split(",") if word.strip()]
    else:
        candidate = words[:]  # fallback case
    return candidate

# Compare two words using ChatGPT-4 to determine correct order.
def compare_pair(word1, word2):
    prompt = (f"Given the two words '{word1}' and '{word2}', "
              "please tell me which word should come first in alphabetical order. "
              "Answer with only the word that should come first.")
    result = call_chatgpt(prompt)
    if result:
        return result.strip().lower() == word1.lower()
    return word1.lower() <= word2.lower()

# Refine the ordering by checking adjacent words.
def refine_sort(candidate):
    corrected = True
    max_iterations = 10
    iteration = 0
    while corrected and iteration < max_iterations:
        corrected = False
        iteration += 1
        for i in range(len(candidate)-1):
            if not compare_pair(candidate[i], candidate[i+1]):
                candidate[i], candidate[i+1] = candidate[i+1], candidate[i]
                corrected = True
                time.sleep(0.5)  # Delay to avoid rate-limits
    return candidate

# Full workflow: coarse sort then refine.
def optimized_alphabetize(words):
    candidate = coarse_sort(words)
    final_sorted = refine_sort(candidate)
    return final_sorted

# Read words from the specified text file
def read_word_list(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        # Assume one word per line; you can adjust if the format is different
        words = [line.strip() for line in f if line.strip()]
    return words

# Main function to process each file in the folder.
def sort_word_lists_from_files():
    folder = "/Users/sahil/Documents/Human-in-the-Loop Computation/Assignment 3/Linear Size Word Lists/Random Lists/"
    filenames = ["list_10.txt", "list_50.txt", "list_100.txt", "list_200.txt"]
    sorted_lists = {}
    for fname in filenames:
        filepath = os.path.join(folder, fname)
        words = read_word_list(filepath)
        print(f"Sorting {len(words)} words from file {fname}...")
        sorted_words = optimized_alphabetize(words)
        sorted_lists[fname] = sorted_words
        # For demonstration, print the first 10 sorted words
        print("First 10 sorted words:", sorted_words[:10])
    return sorted_lists

if __name__ == "__main__":
    gpt_called =0
    sorted_results = sort_word_lists_from_files()
    print("GPT CALLED: ",gpt_called)