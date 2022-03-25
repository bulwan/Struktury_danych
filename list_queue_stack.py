class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, new_data ):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        if(self.head.next==None):
            self.tail=self.head

    def printList(self):
        if (self.head == None):
            print('Lista jest pusta.')
            return
        temp = self.head
        print(temp.data, end='')
        temp = temp.next
        while (temp):
            print (' -> {}'.format(temp.data), end='')
            temp = temp.next
        print(" ")

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

    def node(self, at):
        n=1
        temp = self.head
        while (temp):
            if(n==at):
                return temp
            n = n + 1
            temp = temp.next

    def len(self):
        n=0
        temp = self.head
        while(temp):
            n = n + 1
            temp = temp.next
        return n

    def remove_last(self):    
        if (self.head == None):
            print('Lista jest pusta.')
        elif (self.head.next==None):
            self.head=None
        else:
            temp = self.head
            for _ in range (0,self.len()-2):
                temp=temp.next
            temp.next=None
            self.tail=temp
        return

    def insert(self, data, after):
        new_node = Node(data)
        new_node.next = after.next
        after.next = new_node
        if new_node.next == None:
            self.tail = new_node

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

    def remove_next(self, after):
        if after.next == None:
            print("Nie ma czego usuwac.")
            return
        else:
            after.next = after.next.next
            return

class Stack:
    def __init__(self) -> None:
        self.storage = linkedList()

    def push(self, data) -> None:
        self.storage.append(data)

    def pop(self):
        temp = self.storage.node(self.storage.len())
        self.storage.remove_last()
        return temp
    
    def printstack(self):
        for x in range(self.storage.len(), 0, -1):
            print(self.storage.node(x).data)
        if self.storage.len()==0:
            print('Stos jest pusty.')

    def len(self):
        return self.storage.len()

class Queue:
    def __init__(self) -> None:
        self.storage = linkedList()

    def enqueue(self, data) -> None:
        self.storage.append(data)

    def dequeue(self) -> None:
        temp = self.storage.head
        self.storage.pop()
        return temp

    def peek(self):
        return self.storage.node(1)

    def len(self):
        return self.storage.len()

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


#           L I S T A


# lista = linkedList()
# lista.push(5)
# lista.push(3)
# lista.push(11)
# lista.push(52)
# lista.append(10)
# lista.printList()
# # print(lista.node(5).data) 
# # print(lista.len())
# # lista.remove_last()
# # lista.insert(4, lista.node(5))
# # lista.printList()
# lista.remove_next(lista.node(5))
# lista.printList()


#           S T O S


# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.printstack()
# stack.pop()
# print('stos po kasowaniu:')
# stack.printstack()
# print('liczebnosc stosu:', stack.len())


#           K O L E J K A

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.printqueue()
queue.dequeue()
queue.dequeue()
print("kolejnosc po dwoch usunieciach:")
queue.printqueue()
print("liczebnosc kolejki:", queue.len())





