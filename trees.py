# By: Grace Wanjiru
# TREES IN DATA STRUCTURES
# Demonstrates binary trees, binary search trees (BST), and tree traversals

# -----------------------------
# SIMPLE BINARY TREE
# -----------------------------

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


# -----------------------------
# BINARY SEARCH TREE (BST)
# -----------------------------

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return BSTNode(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


# -----------------------------
# GENERAL TREE
# -----------------------------

class GeneralTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def print_tree(node):
    if node:
        print(node.data)
        for child in node.children:
            print_tree(child)


# -----------------------------
# MAIN EXECUTION
# -----------------------------

if __name__ == "__main__":

    print("Simple Binary Tree Inorder Traversal:")
    root_bt = BinaryTreeNode(1)
    root_bt.left = BinaryTreeNode(2)
    root_bt.right = BinaryTreeNode(3)
    root_bt.left.left = BinaryTreeNode(4)
    root_bt.left.right = BinaryTreeNode(5)

    inorder(root_bt)
    print("\n")

    print("Binary Search Tree Traversals:")
    root_bst = None
    for value in [8, 3, 10, 1, 6, 14]:
        root_bst = insert(root_bst, value)

    print("Inorder:")
    inorder(root_bst)
    print("\nPreorder:")
    preorder(root_bst)
    print("\nPostorder:")
    postorder(root_bst)
    print("\n")

    print("General Tree:")
    root_gt = GeneralTreeNode("A")
    child1 = GeneralTreeNode("B")
    child2 = GeneralTreeNode("C")
    child3 = GeneralTreeNode("D")

    root_gt.children.append(child1)
    root_gt.children.append(child2)
    child1.children.append(child3)

    print_tree(root_gt)
