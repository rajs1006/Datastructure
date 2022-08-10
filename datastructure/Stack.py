class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None
        self.len = 0

    def __len__(self):
        return self.len

    def empty(self):
        return self.len == 0

    def push(self, data):
        node = Node(data)

        node.next = self.head
        self.head = node
        self.len += 1

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
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)

    print(f"Stack: {stack} with size {len(stack)}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")

    print(f"Stack: {stack} with size {len(stack)}")
