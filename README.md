# BST_100

# Implementation of BST in various programming languages

This project consists of implementations of BST (Binary Search Tree) in various programming languages. A BST is a data structure that allows for fast searching, adding, and removing of elements in logarithmic time. Each of the implementations has been performance-tested by performing 10,000,000 additions of numbers to the tree, followed by 20,000,000 checks to see if the tree contains elements.

## Implementations

The project currently includes implementations of BST in the following languages:

- Python

Each implementation is located in a separate directory in the repository.

## Performance tests

The following tests were conducted:

- 10 million elements were added to the tree.
- 20 million checks were performed to see if an element exists.
- The time to count the elements in the tree was measured.
- The height of the tree was calculated.

  Each test was repeated 3 times and then the average was calculated.
  Final BST has 5.000.000 elements and 57 levels

Here are the performance test results for each implementation:

| Language | Version | Add Time (s) | Contains Time (s) | Count Elements Time (s) | Height Time (s) |
| -------- | ------- | ------------ | ----------------- | ----------------------- | --------------- |
| Python   | 3.11.0  | 45.12        | 54.78             | 2.26                    | 2.69            |
| C++      | gcc 12  | 8.01         | 9.55              | 0.38                    | 0.51            |

## Requirements

To run the code in each language, you will need to install the appropriate interpreter and development tools.

## Running the code

To run the code in each language, navigate to the appropriate directory in the repository and run the script or program from the command line.
