# Write a function to see if a binary tree is "superbalanced"

# A tree is "superbalanced" if the difference between the depths of any
# two leaf nodes is no greater than one.

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

def is_leaf(node):
    if node.left is None and node.right is None:
        return True
    else:
        return False

def get_min_max(node, min_depth=None, max_depth=0, depth=0):
    if node is None:
        return min_depth, max_depth
    elif is_leaf(node):
        if min_depth is None:
            min_depth = depth
        else:
            min_depth = min(depth, min_depth)
        max_depth = max(depth, max_depth)
        return min_depth, max_depth
    else:
        min_l, max_l = get_min_max(node.left, min_depth, max_depth, depth + 1)
        min_r, max_r = get_min_max(node.right, min_l, max_l, depth + 1)
        return min_r, max_r

def check_suberbalance(node):
    minim, maxim = get_min_max(node)
    if maxim - minim > 1:
        print "Not a superbalanced tree!"
    else:
        print "Super-balanced tree...yay!"

# create a binary tree
root = BinaryTreeNode(10)
l2 = root.insert_left(5).insert_left(2)
l2.insert_right(4)
root.insert_right(15)

check_suberbalance(root)
