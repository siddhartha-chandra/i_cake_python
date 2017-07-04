# 2nd largest item in a binary search tree
class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def get_largest(node):
    while node.right:
        node = node.right
    return node.value

def find_2nd_largest(node):
    if not node or (not node.left and not node.right):
        raise Exception("Atleast two elements needed for finding 2nd largest number")
    while node.right:
        prev_val = node.value
        node = node.right
    if not node.left:
        return prev_val
    else:
        return get_largest(node.left)

root = BinaryTreeNode(50)
left = root.insert_left(25)
left.insert_left(15)
left.insert_right(30).insert_right(40)
right = root.insert_right(75)
right.insert_left(60)

print find_2nd_largest(root)
