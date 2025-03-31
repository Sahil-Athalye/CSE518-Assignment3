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
