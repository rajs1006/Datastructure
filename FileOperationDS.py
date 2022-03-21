import yaml


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
            raise Exception(f"Node '{parentNode.data}' does not exist !")

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
            raise Exception(f"Node '{parentNode.data}' does not exist !")

        idx, childNode, isChildPresent = self.__getChild(childTree, parentNode)
        if isChildPresent:
            parentNode.child.pop(idx)

    def toDict(self, parent=None, jsonStr={}):

        parent = parent if parent else self

        if parent.child:
            jsonStr[parent.data] = []
            # Inplace sorting for printing
            parent.child.sort(key=lambda c: c.data)
            for i, c in enumerate(parent.child):
                jsonStr[parent.data].append({c.data: []} if c.child else c.data)
                self.toDict(parent=c, jsonStr=jsonStr[parent.data][i])

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


class CommandOperations:
    @staticmethod
    def __addChild(T, path):
        for i in range(len(path) - 1, -1, -1):
            if i == 0:
                T.addChild(path[i], "/")
            else:
                T.addChild(path[i], path[i - 1])

    @staticmethod
    def __removeChild(T, path):
        for i in range(len(path) - 1, -1, -1):
            if path[i].split(".")[-1] != "txt":
                if i == 0:
                    T.removeChild(path[i], "/")
                else:
                    T.removeChild(path[i], path[i - 1])
            else:
                T.removeChild(path[i], path[i - 1])
                break

    @staticmethod
    def __getCommands(line):
        command = line.replace("\n", "")
        cmd = command.split(" ")

        return (cmd[0], cmd[1:])

    def __init__(self) -> None:

        self.__command_dictionary = {
            "md": self.makeFileDirectory,
            "mf": self.makeFileDirectory,
            "mv": self.moveFileDirectory,
            "rm": self.removeFileDirectory,
            "cp": self.copyFileDirectory,
        }
        self.T = Tree("/")

    def __call__(self, commandLine):

        cmd, path = self.__getCommands(commandLine)

        funct = self.__command_dictionary[cmd]
        funct(path, self.T)

    def makeFileDirectory(self, location, T):
        loc = location[0]
        path = loc.split("/")

        newPath = [p for p in path if p]
        self.__addChild(T, newPath)

    def removeFileDirectory(self, location, T):
        loc = location[0]
        path = loc.split("/")

        filteredPath = [p for p in path if p]
        self.__removeChild(T, filteredPath)

    def copyFileDirectory(self, location, T):

        newPath = [p for p in location[1].split("/") if p]
        self.__addChild(T, newPath)

    def moveFileDirectory(self, location, T):
        originalPath = [p for p in location[0].split("/") if p]
        newPath = [p for p in location[1].split("/") if p]

        self.__removeChild(T, originalPath)
        self.__addChild(T, newPath)

    def json(self):
        return self.T.toDict()

    def __str__(self) -> str:
        return yaml.dump(self.json(), default_flow_style=False)


commands = """md /Test
md /Dir1
md /Dir1/Dir2
md /Dir1/Dir2/NewDir
mf /Dir1/Dir2/file.txt
rm /Dir1/Dir2/file.txt
cp /Dir1/Dir2/file.txt /Dir1/Dir2/newfile.txt
mv /Dir1/Dir2/newfile.txt /Dir1/Dir2/newfile1.txt
rm /Dir1/Dir4/newfile.txt
md /Dir3/Dir4/NewDir
"""

if __name__ == "__main__":

    cmdProcessor = CommandOperations()

    for line in commands.splitlines():
        try:
            cmdProcessor(line)
        except Exception as e:
            print(f"'{line}' failed with error {e}")

    print("\n----------- File Structure -------------\n")
    print(str(cmdProcessor))
