# You want to be able to access the largest element in a stack.
# You've already implemented this Stack class:

class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

# Now, use your Stack class to implement a new class MaxStack with a function get_max() that returns the largest element in the stack. get_max() should not remove the item.
#
# Your stacks will contain only integers.


class MaxStack:

    def __init__(self):
        self.stack = Stack()
        self.maxes_stack = Stack()

    # Add a new item to the top of our stack. If the item is greater
    # than or equal to the last item in maxes_stack, it's
    # the new max! So we'll add it to maxes_stack.
    def push(self, item):
        self.stack.push(item)
        if item > self.maxes_stack.peek():
            self.maxes_stack.push(item)

    # Remove and return the top item from our stack. If it equals
    # the top item in maxes_stack, they must have been pushed in together.
    # So we'll pop it out of maxes_stack too.
    def pop(self):
        item = self.stack.pop()
        if item == self.maxes_stack.peek():
            self.maxes_stack.pop()
        return item

    def get_max(self):
        return self.maxes_stack.peek()
