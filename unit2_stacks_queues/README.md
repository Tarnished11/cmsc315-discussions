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

While completing this assignment, I refreshed my knowledge on how stacks and queues work and how to implement them in Python. 
I used a list to build a stack and the collections.deque to build a queue. 
This effectively reinforced the lesson about the difference between Last-In, First-Out and First-In, First-Out behavior.

One challenge I encountered was handling empty stacks and queues. 
Methods such as pop() and dequeue() can cause problems if there are no items to remove. 
I solved this by checking whether the data structure was empty before performing those operations and returning None when appropriate. 
This can be replaced by a custom message later like "No undo tasks available".

Stacks and queues have many real-world applications. 
A stack is useful for features like an Undo button because the most recent action is reversed first. 
A queue is useful for situations like customer support tickets or printer jobs, where requests are processed in the order they are received. 
This assignment helped me understand why choosing the correct data structure is important when solving programming problems. Completing the implementation and testing the edge cases improved my knowledge in working with stacks, queues, and simple data structures in Python.
