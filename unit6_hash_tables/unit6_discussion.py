"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # Creating empty dictionary
    table = {}
    # Adding items
    # A dictionary works like a hash table because it uses a key to calculate
    # where the value is stored, allowing fast lookups.
    table["milk"] = 3.0
    table["eggs"] = 5.0
    table["bread"] = 4.0
    table["sauce"] = 2.5
    table["cereal"] = 4.5

    print(table)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # The lookup works by using the key to quickly find and return
    # its associated value in the dictionary
    print(f"Cereal price is: ${table['cereal']:.2f}")
    print(f"Milk price is: ${table['milk']:.2f}")


    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    # If a key already exists, assigning a new value overwrites the old value,
    # so the dictionary keeps the same key but stores the updated value instead.
    print(f"Price of eggs before update: ${table['eggs']:.2f}")
    table["eggs"] = 6.0
    print(f"Price of eggs after update: ${table['eggs']:.2f}")


    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    # Deleting a key removes both the key and its associated value from the dictionary.
    print("Dictionary before deletion:")
    print(table)
    del table["eggs"]
    print("Dictionary after deletion:")
    print(table)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    empty_dict = {}
    # To look up a missing key, it's better to use the getter method.
    # This way it doesn't raise a KeyError, instead it returns None.
    print(f"Looking up apple in empty dictionary: {empty_dict.get("apple")}")

    # To safely delete a missing key, you could use an if-statement to check if the
    # key exists, or use the pop() method. This returns the second parameter instead of
    # raising an error.
    print(f"Deleting apple from an empty dictionary: {empty_dict.pop("apple", "Key not found")}")

    # ===============================
    # (Student): REAL WORLD SCENARIO
    # ===============================

    print("\n=== REAL WORLD SCENARIO ===")
    print("TODO: Use a dictionary with a real world example.")

    # Using my first dictionary, I can add up all the food prices and display the total.
    total = 0
    print("--- Grocery List ---")
    for key, value in table.items():
        print(f"{key}: ${value:.2f}")
        total += value
    print("-------------")
    print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()