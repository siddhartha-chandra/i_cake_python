# Write a function to check that a binary tree is a valid binary search tree

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

def check_bst(node, parent_value = None):
    if not node.left:
        res_l = True
    else:
        if node.left.value <= node.value:
            res_l = check_bst(node.left, node.value)
        else:
            res_l = False

    if not node.right:
        res_r = True
    else:
        if node.right.value > node.value:
            print "%s, %s" % (node.right.value, parent_value)
            if parent_value == None or node.right.value <= parent_value:
                res_r = check_bst(node.right, None)
            else:
                res_r = False
        else:
            res_r = False
    return res_l and res_r

tree = BinaryTreeNode(50)
l = tree.insert_left(30)
l.insert_left(20)
l.insert_right(60)
r = tree.insert_right(80)
r.insert_left(70)
r.insert_right(90)

print "Is BST: %s" % check_bst(tree)
