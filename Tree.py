class Tree(object): # needs to be run to load the trees
    
    def __init__(self, data, depth=0):
        self.parent = None
        self.depth = depth
        self.child = list()
        self.data = data
        
    def addChild(self, child, parent) :
        ## Convert data to Tree
        parentNode, _ = self.__getChild(parent, self)
        childNode, isPresent = self.__getChild(child, parentNode)
        
        if not isPresent:
            parentNode.child.append(childNode)
            childNode.parent = parentNode
#             print('Appended ', childNode.data, parentNode.data, self.toJson())
            
    def verifyChild(self, testChild):
        isPresentList = []
        alternateParameters = []
        p = self
        for i, child in enumerate(testChild):
            c = Tree(child, depth=i+1)
            c, isPresent =  self.__getChild(c, p)
            
            if not isPresent:
                c = p.child[-1]
                
            alternateParameters.append(c.data)
            isPresentList.append(isPresent)
            p = c
        
        alternateParameters.append(p.child[-1].data)
        
        return alternateParameters, np.all(isPresentList)       
    
    def toJson(self, parent = None, jsonStr = {}):
        
        parent = parent if parent else self
        
        if parent.child:
            jsonStr[parent.data] =  []
            for i, c in enumerate(parent.child):
                
                jsonStr[parent.data].append({c.data : []} if c.child else c.data)
                self.toJson(parent = c, jsonStr=jsonStr[parent.data][i])
            
            return jsonStr
        
    def __getChild(self, child, parent=None, isPresent = False):
        
        if child :
            if self.__equals(child, parent) :
                child = parent
                isPresent = True
            elif parent.child:
                for c in parent.child:
                    child, isPresent = self.__getChild(child, c, isPresent = isPresent)
                    
            return child, isPresent
        else:
            raise Exception('Child not found')
            
    
    def __equals(self, tree1, tree2):
        if (tree1.data == tree2.data) & (tree1.depth == tree2.depth):
            if not tree1.parent: 
                return True
            elif (tree1.parent.data == tree2.parent.data):
                return True
        return False
      
class Tree(object):
    
    def __init__(self, data, depth=0):
        self.depth = depth
        self.child = list()
        self.data = data
        
    def addChild(self, child, parent = None) :
        ## Convert data to Tree
        self.depth = self.depth + 1 if parent else 0
        parentTree = Tree(parent.strip(), self.depth) if parent else self
        childTree = Tree(child.strip(), self.depth + 1)
        
        parentNode, _ = self._getChild(parentTree, self)
        childNode, isPresent = self._getChild(childTree, parentNode)
        print('Addnode ', parentNode.data, childNode.data, isPresent)
        if not isPresent:
            parentNode.child.append(childNode)
            print('Appended ', parentNode.child[-1].data, parentNode.child[-1].depth)
            
        print('------'*10)
            
    def verifyChild(self, testChild):
        t1 = Tree(testChild[1].strip())
        # if isPresent:
        ch1, isPresent = t._getChild(t1, self)
        ch2, isPresent = t._getChild(Tree(testChild[0].strip()), ch1)
        ch3, isPresent = t._getChild(Tree(testChild[2].strip()), ch2)
        
        return isPresent
    
    def toString(self, parent =None, treeStr = []):
        
        parent  = parent if parent else self
        if parent.child:
            for c1 in parent.child:
                if parent.data in treeStr.keys():
                    treeStr[parent.data].append(c1.data)
                else:
                    treeStr[parent.data] = [c1.data]
                    
                self.toString(parent = c1, treeStr = treeStr)
        
            return treeStr
#             for c2 in c1.child:
#                 treeStr = ' : '.join(c2.data)
#                 for c3 in c2.child
        
    def _getChild(self, child, parent=None, isPresent = False, depth=0):
        
        if child :
            print('parent : ', child.data, parent.data)
            if self._equals(child, parent) :
                child = parent
                isPresent = True
            elif parent.child:
                for c in parent.child:
                    print('Child  : ', child.data, c.data)
                    child, isPresent = self._getChild(child, c, isPresent = isPresent)
                    
            return child, isPresent
        else:
            raise Exception('Child not found')
            
    
    def _equals(self, tree1, tree2):
        if (tree1.data == tree2.data) & (tree1.depth == tree2.depth):
            return True
        
        
class Tree(object):
    
    def __init__(self, data, depth=0):
        self.depth = depth
        self.child = list()
        self.data = data
        
    def addChild(self, child, parent) :
        ## Convert data to Tree
        parentNode, _ = self.__getChild(parent, self)
        childNode, isPresent = self.__getChild(child, parentNode)
        
        if not isPresent:
            parentNode.child.append(childNode)
            
    def verifyChild(self, testChild):
        
        t1 = Tree(testChild[1].strip(), depth=1)
        t2 = Tree(testChild[0].strip(), depth=2)
        t3 = Tree(testChild[2].strip(), depth=3)

        # if isPresent:
        ch1, isPresent = t.__getChild(t1, self)
        ch2, isPresent = t.__getChild(t2, ch1)
        ch3, isPresent = t.__getChild(t3, ch2)
        
        return isPresent
    
    def toJson(self, parent = None, jsonStr = {}):
        
        parent = parent if parent else self
        
        if parent.child:
            jsonStr[parent.data] =  []
            for i, c in enumerate(parent.child):
                
                jsonStr[parent.data].append({c.data : []} if c.child else c.data)
                self.toJson(parent = c, jsonStr=jsonStr[parent.data][i])
            
            return jsonStr
        
    def __getChild(self, child, parent=None, isPresent = False):
        
        if child :
            if self.__equals(child, parent) :
                child = parent
                isPresent = True
            elif parent.child:
                for c in parent.child:
                    child, isPresent = self.__getChild(child, c, isPresent = isPresent)
                    
            return child, isPresent
        else:
            raise Exception('Child not found')
            
    
    def __equals(self, tree1, tree2):
        if (tree1.data == tree2.data) & (tree1.depth == tree2.depth):
            return True
        
