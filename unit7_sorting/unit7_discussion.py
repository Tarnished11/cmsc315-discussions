"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Creating a copy so the original list is unchanged.
    copy = lst.copy()

    # Bubble sort repeatedly swaps adjacent elements until the list is sorted.
    # Outer loop controls how many passes happen on the list.
    # Inner loop iterates over each element, comparing values.
    for i in range(len(copy) - 1):
        for j in range(len(copy) - i - 1):
            if copy[j] > copy[j + 1]:
                temp = copy[j]
                copy[j] = copy[j + 1]
                copy[j + 1] = temp
    return copy

def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Base case for recursion is checking if the list has <= 1 elements.
    if len(lst) > 1:

        # Dividing list in half
        left_lst = lst[:len(lst) // 2]
        right_lst = lst[len(lst) // 2:]

        # merge_sort() is called recursively on each of the list segments to
        # continue slicing the list until one element remains in each side.
        left_lst = merge_sort(left_lst)
        right_lst = merge_sort(right_lst)

        # merge() is called on each of the segments.
        lst = merge(left_lst, right_lst)

    # Returns sorted list. Also returns list as-is if merge_sort() is called on
    # a list with a single element.
    return lst

def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    merged = []
    i = 0 # left index
    j = 0 # right index

    # This while-loop happens when both left and right lists have elements remaining.
    while i < len(left) and j < len(right):

        # Checking each element and storing the lesser in `merged`
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        # if right element is lesser, or if elements are equal, storing right element.
        else:
            merged.append(right[j])
            j += 1

    # This while-loop happens when right list is empty but left still has elements.
    while i < len(left):
        merged.append(left[i])
        i += 1

    # This while-loop is when the left is empty.
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    dataset = [4, 2, 7, 12, 3, 72, 35]
    print("Dataset to be sorted:", dataset)
    print("Sorted using Bubble Sort:", bubble_sort(dataset))
    print("Sorted using Merge Sort:", merge_sort(dataset))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    dataset2 = [99, 59, 102, 1, 456, 43, 0]
    print("Second dataset to be sorted:", dataset2)
    print("Sorted using Bubble Sort:", bubble_sort(dataset2))
    print("Sorted using Merge Sort:", merge_sort(dataset2))
    print("Both methods produce an identical sorted list.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    empty_lst = []
    print("\nUsing Bubble Sort on an empty list:", bubble_sort(empty_lst))
    print("The for-loop in bubble_sort() never occurs because range would be -1.")

    print("\nUsing Merge Sort on an empty list:", merge_sort(empty_lst))
    print("The if-statement in the method is false, so the list is returned unchanged.")
    print("\n====================================")
    single = [5]
    print("Using Bubble Sort on a single element list:", bubble_sort(single))
    print("The for-loop in the method doesn't occur because range would be 0.")
    print("\nUsing Merge Sort on a single element list:", merge_sort(single))
    print("The if-statement in the method is false, so the list is returned unchanged.")

    # ===============================
    # REAL-WORLD EXAMPLE
    # ===============================

    print("\n=== REAL-WORLD EXAMPLE ===")
    print("This demonstrates how Merge Sort can sort a list of random grocery prices.")

    prices = [25.5, 19.99, 5.54, 7.25]

    print("\nUnsorted grocery prices:")
    for price in prices:
        print(f"${price:.2f}")

    prices = merge_sort(prices)

    print("\nSorted grocery prices using Merge Sort:")
    for price in prices:
        print(f"${price:.2f}")


if __name__ == "__main__":
    main()