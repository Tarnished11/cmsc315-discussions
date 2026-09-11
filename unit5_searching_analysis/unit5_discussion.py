"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # This is linear search because it is searching the list from beginning to end.
    # The search time grows directly in proportion to n.
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1

    # Each iteration reduces the search space in half because the list is already
    # sorted, so comparisons can be made starting from the middle.
    # Depending on whether the target is less than or greater than the mid point,
    # the opposite half is discarded and the process repeats.
    while low <= high:
        mid = (high + low) // 2
        if target < lst[mid]:
            high = mid - 1
        elif target > lst[mid]:
            low = mid + 1
        else:
            return mid
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Current list:", nums)

    # Linear search is iterating through the list, one-by-one, beginning to the target or end.
    # The index of the target is returned if found, -1 is returned if the search reaches the end
    # without finding the target.
    print("Linear search for 8:", linear_search(nums, 8))
    print("Linear search for 15:", linear_search(nums, 15))

    # Binary search is dividing the search area in half with each iteration.
    # With 8, the mid point index is 4, so the search begins comparing integer 5.
    # 8 is > 5 so the first half of the list is discarded, and a new mid-point of
    # index 7 is selected, which has the integer 8.
    # The "end" of the search is determined by the start and end points of the search space.
    # If the start index is greater than the end, the search reached the end and -1 is returned.
    print("Binary search for 8:", binary_search(nums, 8))
    print("Binary search for 15:", binary_search(nums, 15))


    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    big_nums = list(range(1000))

    # Binary search becomes more efficient as datasets grow larger because
    # it eliminates half of the remaining data with each comparison.
    # For example, searching 1,000 items takes about 10 checks, while
    # searching 1,000,000 items takes only about 20 checks.
    print("Current list is every digit from 0 to 999")
    print("Linear search for 575:", linear_search(big_nums, 575))
    print("Binary search for 575:", binary_search(big_nums, 575))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Both of these will return -1 because that is what's coded into the methods
    # for when a target is not found.
    new_list = []
    print("\nSEARCH EMPTY LIST:")
    print("Linear search for 5:", linear_search(new_list, 5))
    print("Binary search for 5:", binary_search(new_list, 5))

    # Both of these will return the index 0 because the search was successful.
    new_list.append(1)
    print("\nSEARCH SINGLE-ELEMENT LIST:")
    print("Linear search for 1:", linear_search(new_list, 1))
    print("Binary search for 1:", binary_search(new_list, 1))

    print("\n=== REAL-WORLD EXAMPLE ===")
    # Real-world example:
    # A company stores employee IDs in sorted order.
    # Linear search checks each ID one at a time until the correct employee is found.
    # Binary search quickly narrows down the possible IDs by repeatedly cutting the search space in half.
    employee_ids = [1001, 1005, 1010, 1015, 1020, 1025, 1030]

    print("Employee IDs:", employee_ids)

    print("Linear search for ID 1020:", linear_search(employee_ids, 1020))

    print("Binary search for ID 1020:", binary_search(employee_ids, 1020))

if __name__ == "__main__":
    main()