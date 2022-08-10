from Stack import Stack


class Queue:

    """
    Time Complexity:
        Push operation: O(N).
    In the worst case we have empty whole of stack 1 into stack 2.
        Pop operation: O(1).
    Same as pop operation in stack.
        Auxiliary Space: O(N). Use of stack for storing values.

    """

    def __init__(self) -> None:
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enQueue(self, data):

        while len(self.stack1) != 0:
            self.stack2.push(self.stack1.pop())

        self.stack1.push(data)

        while len(self.stack2) != 0:
            self.stack1.push(self.stack2.pop())

    def deQueue(self):
        return self.stack1.pop()


class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.minStack = Stack()

    def push(self, data):

        if self.stack.empty():
            self.stack.push(data)
            self.minStack.push(data)
        else:
            self.stack.push(data)
            minVal = self.minStack.pop()
            self.minStack.push(minVal)

            if data < minVal:
                self.minStack.push(data)

    def getMin(self):

        minNode = 9999
        current = self.stack.head

        while current:
            if current.data < minNode:
                minNode = current.data

            current = current.next

        return minNode

    def getMinPop(self):
        val = self.minStack.pop()
        self.minStack.push(val)

        return val


if __name__ == "__main__":
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())

    s = MinStack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.getMin(), s.getMinPop())
    s.push(5)
    print(s.getMin(), s.getMinPop())
