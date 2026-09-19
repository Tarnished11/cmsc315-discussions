# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Implementation

### Insert Operations
- Created an empty dictionary and added five food items with their prices.
- Demonstrates how dictionaries store data as key-value pairs for fast access.

### Lookup Operations
- Retrieved values using their keys (`cereal` and `milk`).
- Shows how a dictionary quickly finds a value associated with a key.

### Update Operations
- Updated the value of an existing key (`eggs`).
- Demonstrates that assigning a new value to an existing key overwrites the old value.

### Delete Operations
- Removed the `eggs` key-value pair using `del`.
- Shows how entries can be removed from a dictionary.

### Edge Cases
- Looked up a missing key in an empty dictionary using `get()`, which safely returned `None`.
- Deleted a missing key using `pop()` with a default value to prevent a `KeyError`.

### Real-World Scenario
- Used the dictionary as a grocery price list.
- Iterated through all items and calculated the total cost of the groceries.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

## Reflection

In this assignment, I learned how Python dictionaries function similarly to hash tables by storing data as key-value pairs and providing fast access to values through their keys. I also gained experience performing common dictionary operations, including inserting, looking up, updating, and deleting entries. In addition, I learned how to safely handle edge cases such as missing keys by using methods like `get()` and `pop()`.

One challenge I encountered was understanding how the `pop()` method works when deleting a missing key. At first, I thought the second parameter represented another key, but I learned that it is actually a default value that is returned if the requested key does not exist. Experimenting with different examples helped me better understand this behavior.

Hash tables work by using a hash function to determine where data should be stored based on a key. A collision occurs when two different keys map to the same storage location. Hash tables handle collisions internally and still allow data to be accessed efficiently. Because keys can be located directly rather than searching through all entries, hash tables provide fast lookup, insertion, and deletion operations.