# Max-Min Selection Algorithm

Simple Python implementation of an algorithm to find the maximum and minimum values in an array.

This was built as an assignment for the **Foundations of Algorithm Design and Analysis** course at the PUC Minas university.

# About

The Max-Min Selection algorithm is a method to find both the maximum and minimum values in an array using a divide-and-conquer approach. This method is efficient and reduces the number of comparisons needed compared to the naive approach.

The algorithm works by recursively splitting the array into halves, finding the maximum and minimum values in each half, and then combining the results. This approach ensures that the number of comparisons is minimized, making it more efficient for large arrays.

# Structure

This repository contains three `.py` files:

- `maxmin.py`: Contains the implementation of the Max-Min Selection algorithm.
- `test_maxmin.py`: Contains unit tests for the Max-Min Selection algorithm.
- `main.py`: Contains an example of how to use the Max-Min Selection algorithm.

# How to run

You need to have Python 3 installed on your machine to run the code.

To run the example program, you can use the following command:

```bash
python3 main.py
```

To run the unit tests, you can use the following command:

```bash
python3 test_maxmin.py
```

# Control flow graph

![](misc/cyclomatic-complexity.png)
Excalidraw source available [here](misc/cyclomatic-complexity.excalidraw).

## Cyclomatic complexity

Considering `𝑀 = 𝐸 − 𝑁 + 2𝑃`, where 𝐸 is the number of edges (14), 𝑁 is the number of nodes (13), and 𝑃 is the number of connected components (1), the cyclomatic complexity of the Max-Min Selection algorithm is **3**.

## Asymptotic complexity

- **Best case:** `O(1)`, when the array has less then 3 elements.
- **Average/Worst case:**
- **Space complexity:**