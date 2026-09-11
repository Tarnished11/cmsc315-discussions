# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Methods
- **Linear Search** checks elements one at a time and has a worst-case time complexity of **O(n)**.
- **Binary Search** repeatedly cuts the search space in half and has a worst-case time complexity of **O(log n)**.

## Tests
- Searched for existing and non-existing values in a small dataset.
- Searched for a value in a large dataset containing numbers 0-999.
- Tested edge cases:
    - Empty list
    - Single-element list

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

While completing this assignment, I learned how to implement and compare linear search and binary search. I also learned why linear search has a time complexity of O(n) and binary search has a time complexity of O(log n).

2. What challenges did you encounter, and how did you overcome them?

One challenge I encountered was implementing binary search correctly. I initially updated the wrong variable when shrinking the search range, which caused the algorithm to loop endlessly. I fixed the issue by tracing through the code and checking the values of the low, high, and middle indexes.

3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

Linear search is best for small or unsorted datasets because it is simple and works on any list. Binary search is better for large datasets because it finds values much faster by repeatedly cutting the search space in half. However, binary search requires the data to be sorted, while linear search does not. This tradeoff determines which algorithm is more appropriate in different real-world situations.