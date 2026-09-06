"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The value being greater or smaller than the current node matters
        # because it determines whether you go left or right to find where to insert it.
        self.root =  self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case and the step that actually creates a Node.
        if node is None:
            return Node(value)

        # Goes to the left or right of current Node based on if value is < or >.
        elif value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # If value equals current Node, then returns the node unchanged.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search is more efficient because it can eliminate half of the nodes with
        # each comparison. This is more O(log n) average search time versus O(n) for linear.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Base case when path reaches an end and value is not found or value is found.
        if node is None:
            return False
        elif value == node.value:
            return True

        # Compares whether the value is < or > the current node's value.
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Creating an empty list and passing it, along with the root node, to the helper method.
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # Base case of the end of a path.
        if node is None:
            return
        # This traversal returns a sorted output because of BSTs are organized, with each
        # nodes value determining its placement below the parent node.
        # This method starts at the root and traverses all the way left until None is reached,
        # then appends the value to the list. It goes left all the way then attempts to go right
        # one step, before trying to go left all the way again.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)

def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    tree = BST()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    print("Values being inserted: 5, 3, 7, 2, 4, 6, 8")
    print("BST is efficient because each comparison step reduces remaining items by half.")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    print("In-order traversal results: ")
    print(tree.inorder())
    print("In-order traversal produces a sorted output because of how BSTs are built.")
    print("The value being < or > determines its placement, so a recursive method can be")
    print("created to navigate the tree in-order by going to left nodes first before going right.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    print("Below are searches for two values that exist and two that do not.")
    print("True is returned when the value is found, otherwise False is returned.")
    print("Search for 5: ")
    print(tree.search(5))
    print("Search for 3: ")
    print(tree.search(3))
    print("Search for 1: ")
    print(tree.search(1))
    print("Search for 9: ")
    print(tree.search(9))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    empty_tree = BST()
    print("Search an empty tree: ")
    print(empty_tree.search(3))
    print("Inserting duplicate values...")
    empty_tree.insert(3)
    empty_tree.insert(3)
    print("Tree produced: ")
    print(empty_tree.inorder())
    print("The tree produced has only one node because the insert() method doesn't")
    print("allow duplicates. If it sees a duplicate, it returns the node with the")
    print("value already in it.")

if __name__ == "__main__":
    main()