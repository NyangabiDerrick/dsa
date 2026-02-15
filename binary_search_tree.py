# By Benie Macharia
# Binary Search Tree (BST) - O(log n) average case for search/insert/delete
# Left subtree < parent < right subtree

class Node:
    """Node with value and pointers to left and right children"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    """Binary Search Tree implementation"""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST"""
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """Helper method to recursively insert value"""
        if value < node.value:
            # Go left for smaller values
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            # Go right for larger values
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def in_order(self, node):
        """In-order traversal: left -> root -> right (gives sorted order)"""
        if node:
            self.in_order(node.left)
            print(node.value, end=" ")
            self.in_order(node.right)

# Example usage
if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    print("In-order (sorted):")
    bst.in_order(bst.root)
    print()
