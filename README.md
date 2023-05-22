# BST_100

## Implementation of BST in various programming languages

This project consists of implementations of BST (Binary Search Tree) in various programming languages. A BST is a data structure that allows for fast searching, adding, and removing of elements in logarithmic time. Each of the implementations has been performance-tested by performing 5,000,000 additions of numbers to the tree, followed by 10,000,000 checks to see if the tree contains elements.

## Implementations

The project currently includes implementations of BST in the following languages:

- Python3
- C++
- C
- Lua

Each implementation is located in a separate directory in the repository.
All implementations are based on two classes, Node and Tree.

The **Node** class represents a single node in the BST. It contains an integer value and references to its left and right child nodes. The class provides methods to add a value, check if a value is present, calculate the length (number of nodes) in the subtree, and calculate the height (maximum depth) of the subtree.

The **Tree** class serves as the entry point for interacting with the BST. It maintains a reference to the root node of the tree and provides methods to add a value, check if a value is present, calculate the length of the tree, and calculate the height of the tree.

```mermaid
classDiagram
class Node {
    -int value
    -Node left
    -Node right

    +add(int value) bool
    +contain(int value) bool
    +length() bool
    +height() bool
}

class Tree {
    -Node root

    +add(int value) bool
    +contain(int value) bool
    +length() bool
    +height() bool
}
```

In some cases, the implementation may differ depending on the language.

## Performance tests

The following tests were conducted:

- 5 million elements were added to the tree.
- 10 million checks were performed to see if an element exists.
- The time to count the elements in the tree was measured.
- The height of the tree was calculated.

  Each test was repeated 3 times and then the average was calculated.
  Final BST has 5.000.000 elements and 57 levels

Here are the performance test results for each implementation:

![Adding elements](./results/add.jpg)
![Checking elements](./results/check.jpg)
![Counting height of BST](./results/height.jpg)
![Counting elements](./results/len.jpg)

| Language | Version | Add Time (s) | Contains Time (s) | Count Elements Time (s) | Height Time (s) |
| -------- | ------- | ------------ | ----------------- | ----------------------- | --------------- |
| Python   | 3.11.0  | 45.12        | 54.78             | 2.26                    | 2.69            |
| C++      | gcc 12  | 8.01         | 9.55              | 0.38                    | 0.51            |
| C        | c99     | 7.33         | 9.00              | 0.00                    | 0.00            |
| Lua      | 5.4.3   | 41.89        | 48.37             | 2.95                    | 3.36            |
| Rust     | 1.67    | 11.24        | 13.04             | 0.59                    | 0.59            |

## Requirements

To run the code in each language, you will need to have Docker installed.

## Running the code

To run the code in each language, navigate to the appropriate directory in the repository and run `./run.sh`.
