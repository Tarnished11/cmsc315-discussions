# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

# Implementation

## Bubble Sort

The `bubble_sort()` method sorts a copy of the input list using the Bubble Sort algorithm. It repeatedly compares adjacent elements and swaps them when they are out of order. Two nested loops are used, where the outer loop controls the number of passes and the inner loop performs the comparisons and swaps. The method returns a new sorted list while leaving the original list unchanged.

## Merge Sort

The `merge_sort()` method sorts a list using the recursive Merge Sort algorithm. The list is divided into smaller halves until each sublist contains one or zero elements. The `merge()` helper method then combines the sorted sublists by comparing elements from the left and right halves and building a new sorted list. The method returns the fully sorted list in ascending order.

## Merge

The `merge()` helper method combines two already sorted lists into a single sorted list. It compares the current elements from each list, appends the smaller value to a new result list, and continues until one list is exhausted. Any remaining elements are then appended to the result before the merged sorted list is returned.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

## Reflection

While completing this assignment, I learned how to implement and compare two different sorting algorithms: Bubble Sort and Merge Sort. I gained a better understanding of how nested loops can be used to repeatedly compare and swap values in Bubble Sort, as well as how recursion can be used to break a problem into smaller pieces in Merge Sort.

One challenge I encountered was understanding how Merge Sort works through recursive function calls and how the sorted sublists are returned and merged back together. Initially, I was confused about how each recursive call maintained its own variables and returned its results to the previous call. I overcame this challenge by tracing the algorithm step by step with small sample lists and carefully reviewing how the `merge()` helper function combines two sorted lists. This helped me visualize the recursion process and better understand the flow of the algorithm.

Bubble Sort and Merge Sort both produce the same sorted output, but they have different performance characteristics. Bubble Sort is simpler to understand and implement, making it useful for small datasets and learning purposes. However, it requires many comparisons and swaps, giving it a time complexity of O(n²). Merge Sort is more efficient with a time complexity of O(n log n), making it a better choice for larger datasets. The tradeoff is that Merge Sort requires additional memory and is more complex because it uses recursion and temporary lists during the merging process.