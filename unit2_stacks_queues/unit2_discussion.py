"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # By treating the end of the list as the "top", `append` adds items to the top.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # If the stack is empty, pop() returns None, or can be replaced with a message later.
        # Important note here is that items.pop() is calling the pop() method for Python's list.
        if self.items.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # peek() returns the last item in the list, or the "top". Returns None if empty.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        # Checks if the length of `items` is 0, then returns true or false.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Items added to the back of the deque() will be removed last, in the order they were added.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # dequeue() checks if the deque size is 0 by calling is_empty(), then returns None if true.
        # popleft() is from collections.deque and will remove from the "front" of the deque.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # front() returns the item at the "front" of the deque. Returns None if deque is empty.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        # Returns true or false based on if the length of deque is 0.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    print("\n=== STACK DEMO ===")
    print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    print("      test popping from an empty stack,")
    print("      test peeking at an empty stack,")
    print("      and verify a single-item stack becomes empty after removal.")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    stack = Stack()
    # 2. Add at least 4 values to the stack.
    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack.push("D")
    # 3. Improve the print statements so they clearly explain what is happening.
    print("The items added, in order, were: A, B, C, D")
    print(f"The last item added and the top of the stack is: {stack.peek()}")
    # 4. Demonstrate LIFO behavior.
    print("Removing top item...")
    print(stack.pop())
    print(f"Now the top of the stack is: {stack.peek()}")
    # 5. Show what happens when pop() is used on an empty stack.
    emptyStack = Stack()
    print(f"This is what is returned when pop is used on an empty stack: {emptyStack.pop()}")
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    print(f"This is what is returned when peek is used on an empty stack: {emptyStack.peek()}")
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    oneItemStack = Stack()
    oneItemStack.push("A")
    print(f"One item added to new stack: {oneItemStack.peek()}")
    print(f"Removing top item: {oneItemStack.pop()}")
    print(f"Stack contents are now: {oneItemStack.peek()}")

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("TODO: Create a Queue object, demonstrate FIFO behavior,")
print("      test dequeuing from an empty queue,")
print("      test viewing the front of an empty queue,")
print("      and verify a single-item queue becomes empty after removal.")

if __name__ == "__main__":
    main()
