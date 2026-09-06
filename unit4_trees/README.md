# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Implementation

### Binary Search Tree (BST)

The program implements a Binary Search Tree using a `Node` class and a `BST` class. Each node stores a value along with references to its left and right child nodes. New values are inserted recursively, with smaller values placed in the left subtree and larger values placed in the right subtree to maintain BST ordering.

### In-Order Traversal

The BST uses a recursive in-order traversal that visits the left subtree, the current node, and then the right subtree. Because of the BST's structure, this traversal produces values in sorted order.

### Search Operation

Searching is performed recursively by comparing the target value to the current node. Each comparison determines whether to continue searching the left or right subtree, reducing the search space at each step and making searches more efficient than a linear scan.

### Testing

The program demonstrates tree construction, in-order traversal, searching for existing and non-existing values, and several edge cases including searching an empty tree and attempting to insert duplicate values.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

While completing this assignment, I learned how Binary Search Trees organize data using nodes and recursive operations. I gained experience implementing recursive insertion, searching, and in-order traversal methods while improving my understanding of recursion. I also learned how BSTs use comparisons to determine whether a value belongs in the left or right subtree.

2. What challenges did you encounter, and how did you overcome them?

One challenge I encountered was understanding the order in which recursive calls execute. Reading the code alone was not enough for me to visualize what was happening, so I had to trace the recursive calls and think about how they were being pushed onto and removed from the call stack. Once I followed the sequence step by step and drew out the tree structure, it became much easier to understand how recursion navigates the tree and returns back up to previous nodes.

3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

BSTs are efficient because their ordering allows each comparison to eliminate a large portion of the remaining search space. Unlike a linear search that may need to examine every element in a list, a BST can often locate a value by repeatedly moving left or right based on comparisons. This gives BSTs an average search time of O(log n), making them more efficient than many basic data structures when the tree remains balanced.