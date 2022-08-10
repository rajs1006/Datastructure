from Stack import Stack

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, inorderMap, idx) -> None:
        self.inorderMap = inorderMap
        self.idx = idx

    def levelorderConstruct(self, arr, i, n):

        """
        Time Complexity: O(n), where n is the total number of nodes in the tree.

        Space Complexity: O(n) for calling recursion using stack.
        """

        tree = None

        if i < n:
            tree = Node(arr[i])
            tree.left = self.levelorderConstruct(arr, 2 * i + 1, n)
            tree.right = self.levelorderConstruct(arr, 2 * i + 2, n)

        return tree

    def inorderLevelorderConstruct(self, levelorderArr, inorderArr):
        """
        An upper bound on time complexity of above method is O(n3).
        In the main recursive function, extractNodes() is called which takes O(n2) time.

        The code can be optimized in many ways and there may be better solutions.

        Time Complexity: O(n^2)

        Space Complexity: O(n) where n is the number of nodes.
        """

        node = None

        if inorderArr:

            for i in levelorderArr:
                if i in inorderArr:

                    node = Node(i)
                    inorderIdx = inorderArr.index(i)

                    break

            node.left = self.inorderLevelorderConstruct(
                levelorderArr, inorderArr[:inorderIdx]
            )
            node.right = self.inorderLevelorderConstruct(
                levelorderArr, inorderArr[inorderIdx + 1 :]
            )

        return node

    def inorderPreorderConstruct(self, preorderArr, inorderArr):
        """
        Time Complexity: O(n^2). The worst case occurs when the tree is left-skewed.
        Example Preorder and Inorder traversals for worst-case are {A, B, C, D} and {D, C, B, A}.
        """

        node = None

        if inorderArr:

            for i in preorderArr:
                if i in inorderArr:

                    node = Node(i)
                    inorderIdx = inorderArr.index(i)

                    break

            node.left = self.inorderPreorderConstruct(
                preorderArr, inorderArr[:inorderIdx]
            )
            node.right = self.inorderPreorderConstruct(
                preorderArr, inorderArr[inorderIdx + 1 :]
            )

        return node

    def inorderPreorderConstructMap(self, preorderArr, inorderArr):
        """
        Time Complexity: O(n)
        """

        node = None

        if inorderArr:

            inorderCurr = inorderArr[self.idx]
            node = Node(inorderCurr)

            inorderIdx = self.inorderMap[inorderCurr]
            self.idx += 1

            node.left = self.inorderPreorderConstruct(
                preorderArr, inorderArr[:inorderIdx]
            )
            node.right = self.inorderPreorderConstruct(
                preorderArr, inorderArr[inorderIdx + 1 :]
            )

        return node

    def preorderPrint(self, tree):
        if tree:
            print(tree.data)
            self.inorderPrint(tree.left)
            self.inorderPrint(tree.right)

    def inorderPrint(self, tree):

        if tree:
            self.inorderPrint(tree.left)
            print(tree.data)
            self.inorderPrint(tree.right)

    def postorderPrint(self, tree):
        if tree:
            self.inorderPrint(tree.left)
            self.inorderPrint(tree.right)
            print(tree.data)

    def inorderPrintStack(self, tree):

        current = tree
        stack = Stack()

        while True:
            if current:
                stack.push(current)
                current = current.left
            elif not stack.empty():
                current = stack.pop()
                print(current.data)
                current = current.right
                # break
            else:
                break
            
            # print(stack)

        if stack:
            left = stack.pop()
            print(left.data)




    


## Helper method --------


def mapWithIndex(arr):

    mapWithIdx = {}
    for i, v in enumerate(arr):
        mapWithIdx[v] = i

    return mapWithIdx, 0


## Data--------------------

_levelorderConstructTree = [1, 2, 3, 4, 5, 6]

_levelorderConstructTreeForInorderLevelorder = [20, 8, 22, 4, 12, 10, 14]
_inorderConstructTreeForInorderLevelorder = [4, 8, 10, 12, 14, 20, 22]

_inorderConstructTreeForInorderPreorder = ["D", "B", "E", "A", "F", "C"]
_preorderConstructTreeForInorderPreorder = ["A", "B", "D", "E", "C", "F"]

if __name__ == "__main__":

    # tree = Tree()

    # treeInorder = tree.levelorderConstruct(_levelorderConstructTree, 0, len(_levelorderConstructTree))
    # print(tree.inorderPrint(treeInorder))

    # treeInorderLevelorder = tree.inorderLevelorderConstruct(
    #     _levelorderConstructTreeForInorderLevelorder, _inorderConstructTreeForInorderLevelorder
    # )
    # print(tree.inorderPrint(treeInorderLevelorder))

    # treeInorderPreorder = tree.inorderPreorderConstruct(
    #     _preorderConstructTreeForInorderPreorder,
    #     _inorderConstructTreeForInorderPreorder,
    # )
    # print(tree.inorderPrint(treeInorderPreorder))

    ## construct tree using MAP to store the index
    mapWithIdx, idx = mapWithIndex(_inorderConstructTreeForInorderPreorder)
    tree = Tree(mapWithIdx, idx)
    treeInorderPreorder = tree.inorderPreorderConstructMap(
        _preorderConstructTreeForInorderPreorder,
        _inorderConstructTreeForInorderPreorder,
    )
    print(tree.inorderPrint(treeInorderPreorder))
