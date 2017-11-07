# Delete a node from a singly-linked list, given
# only a variable pointing to that node

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

    def display(self):
        ls = [self.value]
        curr_node = self.next
        while curr_node:
            ls.append(curr_node.value)
            curr_node = curr_node.next
        print " -> ".join(ls)

def delete_node(node):
    next_node = node.next
    if not next_node:
        node.value = ''
        node.next = None
    else:
        node.value = next_node.value
        node.next = next_node.next


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

a.display()
delete_node(b)
a.display()

delete_node(a)
a.display()
