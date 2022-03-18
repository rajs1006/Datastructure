import os


class Tree(object):
    def __init__(self, data, depth=0):
        self.parent = None
        self.child = list()
        self.data = data

    def addChild(self, child, parent=None):
        ## Convert data to Tree
        parentTree = Tree(parent.strip()) if parent else self
        childTree = Tree(child.strip())

        _, parentNode, isParentPresent = self.__getChild(parentTree, self)
        if not isParentPresent:
            raise Exception(f"Node {parentNode.data} does not exist !")

        _, childNode, isChildPresent = self.__getChild(childTree, parentNode)
        if not isChildPresent:
            parentNode.child.append(childNode)
            childNode.parent = parentNode

    def removeChild(self, child, parent=None):
        ## Convert data to Tree
        parentTree = Tree(parent.strip()) if parent else self
        childTree = Tree(child.strip())

        _, parentNode, isParentPresent = self.__getChild(parentTree, self)
        if not isParentPresent:
            raise Exception(f"Node {parentNode.data} does not exist !")

        idx, childNode, isChildPresent = self.__getChild(childTree, parentNode)
        if isChildPresent:
            parentNode.child.pop(idx)

    def toJson(self, parent=None, jsonStr={}):

        parent = parent if parent else self

        if parent.child:
            jsonStr[parent.data] = []
            for i, c in enumerate(parent.child):

                jsonStr[parent.data].append({c.data: []} if c.child else c.data)
                self.toJson(parent=c, jsonStr=jsonStr[parent.data][i])

            return jsonStr

    def __getChild(self, child, parent=None, isPresent=False, index=0):

        if child:
            if self.__equals(child, parent):
                child = parent
                isPresent = True
            elif parent.child:
                for i, c in enumerate(parent.child):
                    index, child, isPresent = self.__getChild(
                        child, c, isPresent=isPresent, index=i
                    )

            return index, child, isPresent
        else:
            raise Exception("Child not found")

    def __equals(self, tree1, tree2):
        if tree1.data == tree2.data:
            if not tree1.parent:
                return True
            elif tree1.parent.data == tree2.parent.data:
                return True
        return False


def makeFileDirectory(location, T):
    loc = location[0]
    path = loc.split("/")

    filteredPath = [p for p in path if p]
    for i in range(len(filteredPath)):
        if i == 0:
            T.addChild(filteredPath[i], "/")
        else:
            T.addChild(filteredPath[i], filteredPath[i - 1])

    print(T.toJson())


def removeFileDirectory(location, T):
    loc = location[0]
    path = loc.split("/")

    filteredPath = [p for p in path if p]
    for i in range(len(filteredPath) - 1, -1, -1):
        if filteredPath[i].split(".")[-1] != "txt":
            if i == 0:
                T.removeChild(filteredPath[i], "/")
            else:
                T.removeChild(filteredPath[i], filteredPath[i - 1])
        else:
            T.removeChild(filteredPath[i], filteredPath[i - 1])
            break

    print(T.toJson())


def copyFileDirectory(location, T):

    originalPath = [p for p in location[0].split("/") if p]
    newPath = [p for p in location[1].split("/") if p]

    # NOTE : Not worning on this further
    # newPath.append(originalPath[-1])
    # for i in range(0, len(newPath) - 2):
    #     if i == 0:
    #         T.addChild(newPath[i], "/")
    #     else:
    #         T.addChild(newPath[i], newPath[i - 1])


def moveFileDirectory(location, T):
    copyFileDirectory(location, T)
    removeFileDirectory(location[0], T)


_command_dictionary = {
    "md": makeFileDirectory,
    "mf": makeFileDirectory,
    "mv": moveFileDirectory,
    "rm": removeFileDirectory,
    "cp": copyFileDirectory,
}

a = """md /Test
md /Dir1
md /Dir1/Dir2
md /Dir1/Dir2/NewDir
mf /Dir1/Dir2/file.txt
rm /Dir1/Dir2/file.txt
rm /Dir1/Dir2
"""

if __name__ == "__main__":

    # file = open("a", "r")
    # lines = file.readlines()
    T = Tree("/")

    for line in a.splitlines():
        line = line.replace("\n", "")
        command = line.split(" ")
        funct = _command_dictionary[command[0]]

        print(f"running funct {funct.__name__}")
        funct(command[1:], T)
