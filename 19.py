# Implement a queue using 2 stacks

class QueueTwoStacks:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        self.debug = True

    def enqueue(self, element):
        self.in_stack.append(element)
        if self.debug:
            self.display()

    def dequeue(self):
        if len(self.out_stack) is 0:
            if len(self.in_stack) is 0:
                raise Exception("No elements to dequeue!")

            while len(self.in_stack) > 0:
                popped_element = self.in_stack.pop()
                self.out_stack.append(popped_element)

        self.out_stack.pop()
        if self.debug:
            self.display()
        return

    def display(self):
        print 'In Stack:'
        print ' -> '.join(map(lambda x: str(x), self.in_stack))
        print
        print 'Out Stack:'
        print ' -> '.join(map(lambda x: str(x), self.out_stack))
        print



queue = QueueTwoStacks()
for i in xrange(5):
    queue.enqueue(i)

queue.dequeue()
queue.dequeue()

for i in xrange(1):
    queue.enqueue(i)

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()


# Complexity

# Each enqueue is clearly O(1) time, and so is each dequeue when out_stack has items. Dequeue on an empty out_stack is order of the number of items in in_stack at that moment, which can vary significantly.

# Notice that the more expensive a dequeue on an empty out_stack is (that is, the more items we have to move from in_stack to out_stack), the more O(1)-time dequeues off of a non-empty out_stack it wins us in the future. Once items are moved from in_stack to out_stackthey just sit there, ready to be dequeued in O(1) time. An item never moves "backwards" in our data structure.

# We might guess that this "averages out" so that in a set of m enqueues and dequeues the total cost of all dequeues is actually justO(m). To check this rigorously, we can use the accounting method, ↴ counting the time cost per item instead of per enqueue or dequeue.

# So let's look at the worst case for a single item, which is the case where it is enqueued and then later dequeued. In this case, the item enters in_stack (costing 1 push), then later moves to out_stack (costing 1 pop and 1 push), then later comes off out_stack to get returned (costing 1 pop).

# Each of these 4 pushes and pops is O(1) time. So our total cost per item is O(1). Our m enqueue and dequeue operations put mm or fewer items into the system, giving a total runtime of O(m).
