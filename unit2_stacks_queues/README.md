# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Implementation

### Stack

The `Stack` class uses a Python list as its internal data structure.

Supported operations:
- `push(value)` - Adds an item to the top of the stack.
- `pop()` - Removes and returns the most recently added item.
- `peek()` - Returns the top item without removing it.
- `is_empty()` - Returns `True` if the stack contains no items.

### Queue

The `Queue` class uses `collections.deque` for efficient queue operations.

Supported operations:
- `enqueue(value)` - Adds an item to the back of the queue.
- `dequeue()` - Removes and returns the item at the front of the queue.
- `front()` - Returns the front item without removing it.
- `is_empty()` - Returns `True` if the queue contains no items.

## Testing Performed

### Stack Tests

- Added multiple items and verified LIFO behavior.
- Confirmed that `peek()` displays the current top item.
- Tested `pop()` on an empty stack.
- Tested `peek()` on an empty stack.
- Verified that a single-item stack becomes empty after removal.

### Queue Tests

- Added multiple items and verified FIFO behavior.
- Confirmed that `front()` displays the first item added.
- Tested `dequeue()` on an empty queue.
- Tested `front()` on an empty queue.
- Verified that a single-item queue becomes empty after removal.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.
