import os

# Define the metric functions (they must be consistent with the earlier implementation)

def kendall_tau_rank_correlation(list1, list2):
    """
    Compute the Kendall Tau Rank Correlation between two lists.
    Assumes that list1 and list2 are permutations of the same elements.
    Returns a float between -1 and 1, where 1 means perfect agreement.
    """
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length for Kendall Tau calculation")
    
    n = len(list1)
    rank2 = {elem: i for i, elem in enumerate(list2)}
    concordant = 0
    discordant = 0

    for i in range(n):
        for j in range(i + 1, n):
            a, b = list1[i], list1[j]
            # Check if pair (a,b) is in order in list2
            if (rank2[a] - rank2[b]) * (i - j) > 0:
                concordant += 1
            else:
                discordant += 1

    total_pairs = n * (n - 1) / 2
    tau = (concordant - discordant) / total_pairs
    return tau

def spearman_footrule_distance(list1, list2):
    """
    Compute the Spearman Footrule Distance between two lists.
    Assumes the lists are permutations of the same elements.
    Returns the sum of absolute differences in ranks for each element.
    """
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length for Spearman Footrule calculation")
    
    rank1 = {elem: i for i, elem in enumerate(list1)}
    rank2 = {elem: i for i, elem in enumerate(list2)}

    footrule = sum(abs(rank1[elem] - rank2[elem]) for elem in rank1)
    return footrule

def read_word_list(filepath):
    """
    Reads a text file and returns a list of words.
    Assumes one word per line after stripping whitespace.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]
    return words

def evaluate_sort_metrics(random_folder, sorted_folder):
    """
    For each file in the 'random_folder', this function reads the word list,
    loads the corresponding file (with the same name) from the 'sorted_folder',
    and computes the Kendall Tau Rank Correlation and Spearman Footrule Distance.
    """
    results = {}
    # List all files in the random lists folder
    filenames = os.listdir(random_folder)
    # Only consider text files if necessary:
    filenames = [fname for fname in filenames if fname.endswith(".txt")]

    for fname in filenames:
        path_random = os.path.join(random_folder, fname)
        path_sorted = os.path.join(sorted_folder, fname)
        
        # Ensure that the corresponding file exists in the sorted folder.
        if not os.path.exists(path_sorted):
            print(f"Skipping {fname}: not found in sorted folder.")
            continue

        list_random = read_word_list(path_random)
        list_sorted = read_word_list(path_sorted)

        # Validation: ensure both lists have same content (or size) for valid comparison.
        if len(list_random) != len(list_sorted):
            print(f"Warning for {fname}: lists have different lengths "
                  f"({len(list_random)} vs {len(list_sorted)}). Skipping metric evaluation.")
            continue

        # Calculate the metrics
        tau = kendall_tau_rank_correlation(list_random, list_sorted)
        footrule = spearman_footrule_distance(list_random, list_sorted)

        results[fname] = {"kendall_tau": tau, "spearman_footrule": footrule}
        print(f"File: {fname}")
        print(f"  Kendall Tau Rank Correlation: {tau}")
        print(f"  Spearman Footrule Distance: {footrule}")
        print("-"*40)
    
    return results

if __name__ == "__main__":
    # Define folder paths
    random_folder = "/Users/sahil/Documents/Human-in-the-Loop Computation/Assignment 3/Random Lists"
    one_shot_sorted_folder = "/Users/sahil/Documents/Human-in-the-Loop Computation/Assignment 3/One-Shot Sorted Lists"
    workflow_sorted_folder = "/Users/sahil/Documents/Human-in-the-Loop Computation/Assignment 3/Workflow Sorted Lists"
    truth_folder = "/Users/sahil/Documents/Human-in-the-Loop Computation/Assignment 3/Truth Lists"

    # Evaluate metrics for the one-shot sorted lists
    print("\n***Evaluating One-Shot Sorted Lists vs. Ground Truth: ***\n")
    metrics_results1 = evaluate_sort_metrics(truth_folder, one_shot_sorted_folder)

    print("\n***Evaluating Workflow Sorted Lists vs. Ground Truth: ***\n")
    metrics_results2 = evaluate_sort_metrics(truth_folder, workflow_sorted_folder)
    
    print("\n***Evaluating Workflow Sorted Lists vs. One-Shot Sorted Lists: ***\n")
    metrics_results3 = evaluate_sort_metrics(one_shot_sorted_folder, workflow_sorted_folder)