# Human-in-the-Loop Sorting Workflow

This repository implements a human-in-the-loop sorting workflow that leverages ChatGPT to alphabetize word lists, refine their order, and evaluate the results against ground truth data. The project includes scripts for generating random word lists, sorting them using both automated and human-in-the-loop methods, and calculating metrics to assess sorting accuracy.

## Features

- **Random List Generation**: Generate random word lists of specified sizes.
- **Sorting Methods**:
  - **One-Shot Sorting**: Directly sort word lists using ChatGPT.
  - **Workflow Sorting**: Refine sorting through iterative human-in-the-loop adjustments.
- **Evaluation Metrics**:
  - **Kendall Tau Rank Correlation**: Measures the agreement between two rankings.
  - **Spearman Footrule Distance**: Computes the sum of rank differences between two lists.

## Repository Structure
Assignment 3/ ├── Random Lists/ # Randomly generated word lists ├── Truth Lists/ # Ground truth sorted word lists ├── One-Shot Sorted Lists/ # Word lists sorted in one step using ChatGPT ├── Workflow Sorted Lists/ # Word lists sorted using the human-in-the-loop workflow ├── Linear Size Word Lists/ # Word lists of varying sizes for testing ├── alphabetizeWorkflow.py # Main script for sorting word lists ├── calculateError.py # Script to compute evaluation metrics ├── createLists.py # Script to generate random word lists ├── generateTruth.py # Script to generate ground truth sorted lists └── README.md # Documentation for the repository
