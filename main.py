"""def fibonacci(n):
    if n < 1:
        return "Invalid Output"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.next = None

    def print_recursion(self, node):
        if node is None:
            return
        print(node.data)
        self.print_recursion(node.next)

if __name__ == "__main__":
    print(fibonacci(6))"""

    #LinkedList = LinkedList(None)
"""
#LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last.next = new_node

    def print_recursion(self, node):
        if node is Node:
            return
        print(node.data)
        self.print_recursion(node.next)

    def start_recursion_traversal(self):
        self.print_recursion(self.head)

if __name__ == "__main__":
    linklist = LinkedList()

    linklist.insert(1)
    linklist.insert(2)
    linklist.insert(3)
    linklist.insert(4)
    linklist.insert(5)

    print("Linked List: ")
    linklist.start_recursion_traversal()
    linklist.print_recursion()
"""
# TREE
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# In-Order Traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Pre-Order Traversal
def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Post-Order Traversal
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

# Reverse Traversals
def reversed_inorder_traversal(root):
    if root:
        reversed_inorder_traversal(root.right)
        print(root.value, end=" ")
        reversed_inorder_traversal(root.left)

def reversed_preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        reversed_preorder_traversal(root.right)
        reversed_preorder_traversal(root.left)

def reversed_postorder_traversal(root):
    if root:
        reversed_postorder_traversal(root.right)
        reversed_postorder_traversal(root.left)
        print(root.value, end=" ")

def swap_subtrees(root):
    if root:
        root.left, root.right = root.right, root.left
        swap_subtrees(root.left)
        swap_subtrees(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("In-Order Traversal:")
inorder_traversal(root)
print("\nPre-Order Traversal:")
preorder_traversal(root)
print("\nPost-Order Traversal:")
postorder_traversal(root)

print("\n\nSwapping Subtrees...")
swap_subtrees(root)

print("\nInorder Traversal After Swap:")
inorder_traversal(root)
print("\nPreorder Traversal After Swap:")
preorder_traversal(root)
print("\nPostorder Traversal After Swap:")
postorder_traversal(root)
