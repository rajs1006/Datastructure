from BinaryTree import Node as TreeNode
from Queue import Queue


class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self) -> None:
        self.top = None

    def push(self, data):

        newNode = Node(data)
        newNode.next = self.top

        self.top = newNode

    def append(self, new_value):

        # Allocate new node
        new_node = Node(new_value)

        # if head is None, initialize it to new node
        if self.top is None:
            self.top = new_node
            return
        curr_node = self.top
        while curr_node.next is not None:
            curr_node = curr_node.next

        # Append the new node at the end
        # of the linked list
        curr_node.next = new_node

    def delete(self, val):
        current = self.top
        previous_ = None
        while current:
            if current.value == val:
                if previous_ and current.next:
                    previous_.next = current.next

            previous_ = current
            next_ = current.next

            current = next_

    def recursiveCheckPalindrom(self, right):

        if right:
            isPalindrom = self.checkPalindrom(right.next)

            if isPalindrom == False:
                return False

            isValueEqual = self.top.value == right.value

            self.top = self.top.next

            return isValueEqual

    def checkPalindrom(self, data):

        pushCurrent = data
        stack = []
        while pushCurrent:
            stack.append(pushCurrent.value)
            pushCurrent = pushCurrent.next

        popCurrent = data
        while popCurrent:
            val = stack.pop()
            if val != popCurrent.value:
                return False

            popCurrent = popCurrent.next
        return True

    def removeDuplicates(self):

        current = self.top

        while current.next:
            if current.value != current.next.value:
                # print("2 ", current.value, previous.value)
                current = current.next
            else:
                new = current.next.next
                # current.next = None
                current.next = new

        return self.top

    @staticmethod
    def getStartAndEnd(llist):
        bottom = llist
        while bottom.next != None:
            bottom = bottom.next

        return llist, bottom

    @staticmethod
    def getMiddle(llist):
        single = llist
        double = llist

        while double.next and double.next.next:
            single = single.next
            double = double.next.next

        return single

    @staticmethod
    def print(llist):
        val = []
        current = llist.top
        while current:
            val.append(current.value)

            next_ = current.next
            current = next_

        return f"{val}"

    def __str__(self):
        val = []
        current = self.top
        while current:
            val.append(current.value)

            next_ = current.next
            current = next_

        return f"{val}"


class SinglyLinkedListQuickSort(SinglyLinkedList):
    def paritionLast(self, start, end):

        pivot = start
        current = start
        pivotVal = end.value

        while start != end:
            if start.value < pivotVal:

                pivot = current
                # swap node values only of current with start, oo need to swap next
                # as the next pointer is going to be same just the value of those
                # nodes need to be changed
                (current.value, start.value) = (start.value, current.value)
                current = current.next

            start = start.next

        # put pivot at the the end of list of smaller elements.
        (end.value, current.value) = (current.value, pivotVal)

        # Return one step before Pivot element
        return pivot

    def sort(self, start, end):

        if start != end:

            # split list and partition recurse
            pivot = self.paritionLast(start, end)
            self.sort(start, pivot)

            if pivot != None:

                if pivot == start:
                    # if pivot becomes the first node then start from the next node
                    self.sort(pivot.next, end)
                elif pivot.next != end:
                    # if pivot is in between nodes, then pivot.next will be pivotVal
                    # so start from one node next to pivot val
                    self.sort(pivot.next.next, end)


class SinglyLinkedListMergeSort(SinglyLinkedList):
    def sort(self, high):

        if high is None or high.next is None:
            return high
        # print(f"start : high : {high.value}")
        middle = self.getMiddle(high)
        low = middle.next

        # marking the reference of middle as None as this should be the last node
        middle.next = None
        # print(f"before : high {high.value}, low {low.value}, middle {middle.value}")
        left = self.sort(high)
        # print(f"after left : high {high.value}, low {low.value}, middle {middle.value} , left {left.value}")
        right = self.sort(low)
        # print(f"after right : high {high.value}, low {low.value}, middle {middle.value} , left {left.value}. right {right.value}")
        sortedList = self.merge(left, right)
        # print("sort ", sortedList.value)
        return sortedList

    def merge(self, left, right):

        result = None
        # print("====", left.value if left else None, right.value if right else None, result.value if result else None)
        if not left:
            return right

        if not right:
            return left

        if left.value < right.value:
            result = left
            # print("----", result.value)
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
        # print("after rec merge ", result.value)
        return result

class SinglyLinkedListBinaryTree(SinglyLinkedList):

    def __init__(self) -> None:
        super().__init__()

        self.root = None

    def convertToBinaryTree(self):
        
        queue = Queue()

        if not self.top:
            return 

        self.root = TreeNode(self.top.value)
        queue.push(self.root)

        self.top = self.top.next
        
        while self.top:

            parent = queue.pop()

            left = None
            right = None

            left = TreeNode(self.top.value)
            queue.push(left)
            self.top = self.top.next
            if self.top:
                right = TreeNode(self.top.value)
                queue.push(right)
                self.top = self.top.next

            parent.left = left
            parent.right = right


        # print(parent.data, parent.left.data, parent.left.left.data)

    def inorderPrint(self, tree):

        if tree:
            self.inorderPrint(tree.left)
            print(tree.data)
            self.inorderPrint(tree.right)


if __name__ == "__main__":

    ## data to check palindrom
    # data = ["a", "b", "a", "c", "a", "b", "a"]
    
    ## data to remove duplicate
    # data = [1, 1, 1, 2, 3]

    ## Data for sorting
    data = [4, 1, 2, 8, 5]

    llistM = SinglyLinkedListMergeSort()
    for i in data:
        llistM.push(i)

    llistM.top = llistM.sort(llistM.top)
    print(f"Sorted list MERGE SORT {llistM}")

    llistQ = SinglyLinkedListQuickSort()
    for i in data:
        llistQ.append(i)

    start, end = llistQ.getStartAndEnd(llistQ.top)
    llistQ.sort(start, end)
    print(f"Sorted list QUICK SORT {llistQ}")

    # data for binary tree
    data = [36, 30, 25, 15, 12, 10]

    llistT = SinglyLinkedListBinaryTree()
    for i in data:
        llistT.push(i)

    llistT.convertToBinaryTree()
    print(f"INORDER Binary Tree fo the list {llistT.inorderPrint(llistT.root)}")

    # llist = SinglyLinkedList()
    # llist.removeDuplicates()
    # print(f"final list after removal of duplicates {llist}")

    # isPalindrom = llist.checkPalindrom(llist.top)
    # print(f"{llist} is pallidrom? -> {isPalindrom}")
