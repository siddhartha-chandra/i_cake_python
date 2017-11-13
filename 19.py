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
