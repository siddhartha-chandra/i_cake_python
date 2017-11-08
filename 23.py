# You have a singly-linked list and want to check if it contains a cycle.
# A cycle occurs when a node’s next points back to a previous node in the list.
# The linked list is no longer linear with a beginning and end—instead,
# it cycles through a loop of nodes.

# Write a function contains_cycle() that takes the first node in a singly-linked list and returns a boolean indicating whether the list contains a cycle.

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


# A -> B -> C -> D -> E
#           ^    |
#           |    V
#           Y <- X

def contains_cycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
