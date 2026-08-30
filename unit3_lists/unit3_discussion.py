"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # After insertion occurs, existing elements are shifted either left or right based on where the value was inserted.
    # Python's built-in insert() method handles an index that doesn't exist on its own.
    # Insertion performance is O(n) in the worst case because elements may need to be shifted.
    # Inserting at the end requires no shifts, inserting at the beginning requires all elements to be shifted.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Index validation is important because it prevents an IndexError by pop().
    # Safe deletion also prevents errors and ensures the intended index is deleted.
    if 0 <= index < len(lst):
        return lst.pop(index)
    else:
        return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is linear search because it checks each element one at a time from beginning to the value or end.
    # It scans sequentially because no information is given about where the value may be.
    for i in range(len(lst)):
       if lst[i] == value:
           return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    list = [1, 2, 3, 4, 5]
    print(f"New list created: {list}")
    print("Below, a value will be inserted at the beginning, middle, and end.")
    insert_at(list, 0, 10)
    print(list)
    insert_at(list, 3, 11)
    print(list)
    insert_at(list, 7, 12)
    print(list)
    print("The insert_at() method simply uses Python's built-in insert() method.")
    print("If an out-of-bounds index is used, then insert() uses the closest valid index.")
    print("For example, if index 99 was used on the list above, the value would be inserted at the end.")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    print(f"List at the start: {list}")
    print(f"Deleting from the beginning: {delete_at(list, 0)}")
    print(f"Updated list: {list}")
    print(f"Deleting from the middle: {delete_at(list, len(list) // 2)}")
    print(f"Updated list: {list}")
    print(f"Deleting from the end: {delete_at(list, len(list) - 1)}")
    print(f"Updated list: {list}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    list = [1, 2, 3, 4, 5]
    print(f"Resetting list to: {list}")
    print(f"Searching for index of value 5: {search_value(list, 5)}")
    print(f"Searching for index of value 20: {search_value(list, 20)}")
    print("5 was found, but 20 was not. -1 means that the value was not found.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")
    empty = []

    print(f"List being used: {list}")
    print(f"Attempting to delete index 8: {delete_at(list, 8)}")
    print("None was returned because the index was invalid.")
    print(f"Searching for value 5 in an empty list: {search_value(empty, 5)}")
    print("-1 was returned because value does not exist.")
    print("This can be built upon when used in another program to return a message, or do something else.")

if __name__ == "__main__":
    main()