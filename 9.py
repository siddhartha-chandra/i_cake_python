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

def check_bst(node):
    if node.left:
        if node.left.value <= node.value:
            check_bst(node.left)
        else:
            return False
    if node.right:
        if node.right.value > node.value:
            check_bst(node.right)
        else:
            return False
    return True

tree = BinaryTreeNode(50)
tree.insert_left(25)
tree.insert_right(51)

print "Is BST: %s" % check_bst(tree)
