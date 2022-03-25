from enum import Enum
from typing import Dict, Optional
import graphviz as gv
import os

from graphviz import sources
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

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

    def get_first_node(self):
        return self.storage.node(1).data

    def get_last_node(self):
        return self.storage.node(self.len()).data

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

    def get_first(self):
        return self.storage.node(1)

class EdgeType(Enum):
    def __init__(self) -> None:
        self.directed = 1
        self.undirected = 2

class Vertex:
    def __init__(self, data, index) -> None:
        self.data = data
        self.index = index

class Edge:
    def __init__(self, source, destination) -> None:
        self.source = source
        self.destination = destination
        self.weight = Optional[float]

class Graph:
    def __init__(self) -> None:
        self.adjacencies = {}

    def create_vertex(self, data):
        self.adjacencies[Vertex(data, self.get_index() )]=list()

    def add_directed_edge(self, source, destination, weight):
        self.adjacencies[source].append(Edge(source, destination))

    def add_undirected_edge(self, source, destination, weight):
        self.adjacencies[source].append(Edge(source, destination))
        self.adjacencies[destination].append(Edge(destination, source))

    def add(self, edge, source, destination, weight):
        if edge == 1:
            self.add_directed_edge(source, destination, weight)
        elif edge == 2:
            self.add_undirected_edge(source, destination, weight)
        else:
            return None

    def __str__(self) -> str:
        print("id:\tdata:\tidzie do:")
        key_list = list(self.adjacencies.keys())
        values_list = list(self.adjacencies.values())
        i=0
        for x in key_list:
            print(x.index, "\t", x.data, "\t", end="")
            pomoc = values_list[i]
            for y in range (0, len(pomoc)):
                print(pomoc[y].destination.data, end=", ")
            print("")
            i = i + 1
        return " "
    
    def traverse_breadth_first(self):
        visited = list()
        key_list = list(self.adjacencies.keys())
        print(key_list[0].data)
        que = Queue()
        que.enqueue(key_list[0])
        while que.len()>0:
            v = que.get_first_node()
            visited.append(v)
            for x in self.adjacencies[v]:
                pomoc = 0
                for y in range (0, len(visited)):
                    if visited[y]==x.destination:
                        pomoc = 1
                if pomoc == 0:
                    print(x.destination.data)
                    visited.append(x.destination)
                    que.enqueue(x.destination)
            que.dequeue()

    def traverse_depth_first(self, v, visited=list()):
        pomoc = 0
        for y in range (0, len(visited)):
            if visited[y]==v:
                pomoc = 1
        if pomoc==0:
            visited.append(v)
            print(v.data)
            for x in self.adjacencies[v]:
                self.traverse_depth_first(x.destination, visited)

    def get_index(self):
        return len(self.adjacencies)

def show(self):
    do = gv.Digraph()
    for x in self.adjacencies:
        index = str(x.index)
        data = str(x.data)
        do.node(index, data)
    for x in self.adjacencies:
        for y in self.adjacencies[x]:
            source = str(y.source.index)
            destination = str(y.destination.index)
            do.edge(source, destination)
    do.render(directory='doctest-output', view=True) 

class GraphPath:
    def __init__(self, obiekt, start, koniec) -> None:
        self.graph = obiekt
        self.poczatek = start
        self.koniec = koniec

    def wyszukwanie(self):
        visited = list()
        sciezki = Queue()
        sciezka = []
        sciezka.append(self.poczatek)
        sciezki.enqueue(sciezka)
        visited.append(self.poczatek)
        while(sciezki.len()>0):
            biezaca_sciezka = sciezki.dequeue().data
            biezacy_wierzcholek = biezaca_sciezka[-1]
            for x in self.graph.adjacencies[biezacy_wierzcholek]:
                pomoc = 0
                for y in range (0, len(visited)):
                    if visited[y].data==x.destination.data:
                        pomoc = 1
                if pomoc == 0:
                    nowa_sciezka = []
                    for c in biezaca_sciezka:
                        nowa_sciezka.append(c)
                    nowa_sciezka.append(x.destination)
                    visited.append(x.destination)
                    sciezki.enqueue(nowa_sciezka)
                    if x.destination==self.koniec:
                        for z in nowa_sciezka:
                            print(z.data)


 

# graf = Graph()
# graf.create_vertex("v0")
# graf.create_vertex("v1")
# graf.create_vertex("v2")
# graf.create_vertex("v3")
# graf.create_vertex("v4")
# graf.create_vertex("v5")
# key_list = list(graf.adjacencies.keys())
# graf.add_directed_edge(key_list[0], key_list[1], 10)
# graf.add_directed_edge(key_list[0], key_list[5], 10)
# graf.add_directed_edge(key_list[2], key_list[1], 10)
# graf.add_directed_edge(key_list[2], key_list[3], 10)
# graf.add_directed_edge(key_list[3], key_list[4], 10)
# graf.add_directed_edge(key_list[4], key_list[1], 10)
# graf.add_directed_edge(key_list[4], key_list[5], 10)
# graf.add_directed_edge(key_list[5], key_list[1], 10)
# graf.add_directed_edge(key_list[5], key_list[2], 10)
# # print(graf)
# show(graf)

graf = Graph()
graf.create_vertex("A")
graf.create_vertex("B")
graf.create_vertex("C")
graf.create_vertex("D")
key_list = list(graf.adjacencies.keys())
poczatek = graf.adjacencies[key_list[0]]
graf.add_directed_edge(key_list[0], key_list[1], 30)
graf.add_directed_edge(key_list[1], key_list[3], 2)
graf.add_directed_edge(key_list[0], key_list[2], 10)
graf.add_directed_edge(key_list[2], key_list[3], 9)
graf.add_directed_edge(key_list[2], key_list[1], 5)
# print(poczatek)

szukana = GraphPath(graf, key_list[0], key_list[3])
szukana.wyszukwanie()




