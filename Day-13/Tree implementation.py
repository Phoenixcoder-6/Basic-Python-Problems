class tree:
    def __init__(self,data=None,parent=None):
        self.data=data
        self.children=[]
        self.parent=parent

    def set_root(self,data):
        self.data=data
    
    def add(self,node):
        self.children.append(node)

    def search(self,data):
        if self.data==data:
            return self
        for child in self.children:
            temp=child.search(data)
            if temp is not None:
                return temp
        return None
    def display(self,level=0):
        print(' '*level*2 + str(self.data))
        for child in self.children:
            child.display(level+1)


if __name__=="__main__":
    #Create the root node
    root= tree('A')
    #Add children to the root
    root.add(tree('B'))
    root.add(tree('C'))
    root.add(tree('D'))

    #Add children to child B
    root.children[0].add(tree('E'))
    root.children[0].add(tree('F'))

    #Add children to child C
    root.children[1].add(tree('G'))
    root.children[1].add(tree('H'))

    #Add children to child D
    root.children[2].add(tree('I'))

    print("Tree structure")
    root.display()







