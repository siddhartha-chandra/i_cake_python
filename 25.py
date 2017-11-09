# Write a function kth_to_last_node() that takes an integer kk and the head_node of a singly-linked list, and returns the kkth to last node in the list.

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

def kth_to_last_node(k, head_node):
    slow_node = head_node
    fast_node = head_node
    while k > 0:
        if not fast_node:
            raise ValueError(
                'k is larger than the length of the linked list: %s' % k
                )
        fast_node = fast_node.next
        k -= 1
    while fast_node:
        slow_node = slow_node.next
        fast_node = fast_node.next
    return slow_node

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

res = kth_to_last_node(2, a)
res.value
