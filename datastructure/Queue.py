class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.len = 0

    def size(self):
        return self.len

    def empty(self):
        return self.len == 0

    def push(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next

        self.len += 1
        current.next = node

    def pop(self):

        current = self.head
        self.head = self.head.next
        current.next = None

        self.len -= 1
        return current.data

    def __str__(self):

        r = []
        current = self.head
        while current:
            r.append(current.data)
            current = current.next

        return f"{r}"


if __name__ == "__main__":
    queue = Queue()
    for i in range(1, 11):
        queue.push(i)

    print(f"Queue: {queue} with size {queue.size()}")

    for _ in range(1, 6):
        remove = queue.pop()
        print(f"Pop: {remove}")

    print(f"Queue: {queue} with size {queue.size()}")
