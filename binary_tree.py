class BinaryNode:
    def __init__(self,value) -> None:
        self.value=value
        self.right_child = None
        self.left_child = None
        self.visited = False


    def is_leaf(self):
        if self.right_child==None and self.left_child==None:
            return True
        else:
            return False

    def visit(self):
        self.visited=True

    def add_left(self,value):
        self.left_child = BinaryNode(value)

    def add_right(self,value):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self):
        if self.left_child!=None:
            self.left_child.traverse_in_order()
        print(self.value)
        if self.right_child!=None:
            self.right_child.traverse_in_order()

    def traverse_post_order(self):
        if self.left_child!=None:
            self.left_child.traverse_post_order()
        if self.right_child!=None:
            self.right_child.traverse_post_order()
        print(self.value)
            
    def traverse_pre_order (self):
        print(self.value)
        if(self.left_child!=None):
            self.left_child.traverse_pre_order()
        if(self.right_child!=None):
            self.right_child.traverse_pre_order()

    def __str__(self):
        return str(self.value)

class BinaryTree:
    def __init__(self,value):
        self.root=BinaryNode(value)

    def traverse_in_order(self):
        self.root.traverse_in_order()
    
    def traverse_post_order(self):
        self.root.traverse_post_order()

    def traverse_pre_order(self):
        self.root.traverse_pre_order()
    
    def add_left(self,value):
        self.root.left_child = BinaryNode(value)

    def add_right(self,value):
        self.root.right_child = BinaryNode(value)



tree = BinaryTree(10)
tree.add_left(9)
tree.add_right(2)
tree.root.left_child.add_left(1)
tree.root.left_child.add_right(3)
tree.root.right_child.add_left(4)
tree.root.right_child.add_right(6)
print("travese in order:")
tree.traverse_in_order()
print("travese post order:")
tree.traverse_post_order()
print("travese pre order:")
tree.traverse_pre_order()




    
