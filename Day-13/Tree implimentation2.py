class tree:
    def __init__(self,data=None,parent=None):
        self.data=data
        self.children=[]
        self.parent=parent

    def set_root(self,data):
        self.data=data

    def add(self,node):
        self.children.append(node)
    
    def display(self,level=0):
        print(' ' * level * 2 + str(self.data))
        for child in self.children:
            child.display(level+1)


if __name__=="__main__":
    #create the root node
    root=tree('A')
    #create the child nodes
    root.add(tree('B'))
    root.add(tree('C'))
    #create the children of child B
    root.children[0].add(tree('E')) 
    root.children[0].add(tree('F'))
    #create the children of child C
    root.children[1].add(tree('G'))

    print("Tree Structure")
    root.display()   



