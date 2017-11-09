# Write a function for reversing a linked list. Do it in-place.
#
# Your function will have one input: the head of the list.
# Your function should return the new head of the list.

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


def reverse(head):
    previous = None
    current = head
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous



a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
a.next = b
b.next = c

a.display()
rev_head = reverse(a)
rev_head.display()
