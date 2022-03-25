class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
        last=last.next
        self.tail = last

    def pop(self):
        if self.head == None:
            print("Nie ma czego usuwac.")
            return
        elif self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            return temp
            
        else:
            temp = self.head
            self.head = self.head.next
            return temp

class Queue:
    def __init__(self) -> None:
        self.storage = linkedList()

    def enqueue(self, data) -> None:
        self.storage.append(data)

    def dequeue(self) -> None:
        temp = self.storage.head
        self.storage.pop()
        return temp

    def printqueue(self):
        if (self.storage.head == None):
            print('Kolejka jest pusta.')
        else:
            temp = self.storage.head
            print(temp.data, end='')
            temp = temp.next
            while (temp):
                print (', {}'.format(temp.data), end='')
                temp = temp.next
            print(" ")

class TreeNode:
    def __init__(self,value) -> None:
        self.value=value
        self.children=[]
        self.visited=False

    def add(self,child):
        self.children.append(child)

    def is_leaf(self):
        if self.children==None:
            return True
        else:
            return False

    def visit(self):
        self.visited=True

    def for_each_deep_first(self):
        print(self.value)
        for x in self.children:
            if x.visited==False:
                x.for_each_deep_first()

    def for_each_level_order(self):
        q = Queue()
        last = self
        while last.visited==False:
            q.enqueue(last.value)
            for x in last.children:
                q.enqueue(x.value)
                last = x
                last.visit()
        q.printqueue()
        
    def search(self, data):
        if self.value==data:
            return "biezacy wezel ma szukana wartosc"
        else:
            for x in self.children:
                if x.value==data:
                    return "dziecko biezacego wezlu ma szukana wartosc"
        return "nie ma szukanej wartosci"

    def __str__(self):
        return str(self.value)
    
class Tree:
    def __init__(self,value):
        self.root=TreeNode(value)

    def add(self,value,parent_value):
        q = Queue()
        q.enqueue(self.root)
        if(q.storage.head.data.value==parent_value):
            self.root.children.append(TreeNode(value))
            return None

        while(q.storage.head!=None):
             for x in q.storage.head.data.children:
                 if (x.value==parent_value):
                     x.add(TreeNode(value))
                     return None
                 q.enqueue(x)
             q.dequeue()
    
    def for_each_level_order(self):
        self.root.for_each_level_order()

    def for_each_deep_first(self):
        self.root.for_each_deep_first()


# drzewo=TreeNode('F')
# drzewo.add(TreeNode('B'))
# drzewo.add(TreeNode('G'))
# drzewo.children[0].add(TreeNode('A'))
# drzewo.children[0].add(TreeNode('D'))
# drzewo.children[1].add(TreeNode('I'))
# drzewo.children[0].children[1].add(TreeNode('C'))
# drzewo.children[0].children[1].add(TreeNode('E'))
# drzewo.children[1].children[0].add(TreeNode('H'))
# print(drzewo.search("E"))


# drzewo.for_each_deep_first()
# drzewo.for_each_level_order()
        
drzewo=Tree("F")
drzewo.add("B","F")
drzewo.add("G","F")
drzewo.add("A","B")
drzewo.add("D","B")
drzewo.add("C","D")
drzewo.add("E","D")
drzewo.add("I","G")
drzewo.add("H","I")
drzewo.for_each_deep_first()
