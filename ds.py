# lets practice some important data structures in python
# list,tuple,set,dict,linked list,stack,queue,tree,graph, hash table, heap , etc.
# 1)List: A list is a collection of items that are ordered and changeable. In Python, lists are written with square brackets.
l1 = [1, 2, 3, 4, 5]
print(l1)
print(l1[0])
# methods of list
l1.append(6)
print(l1)
l1.insert(0, 0)
print(l1)
l1.remove(0)
print(l1)
l1.pop()
print(l1)
l1.clear()
print(l1)
# loop through list
l1 = [1, 2, 3, 4, 5]
for i in l1:
    print(i)
# 2)Tuple: A tuple is a collection of items that are ordered and unchangeable. In Python, tuples are written with round brackets.
t1 = (1, 2, 3, 4, 5)
print(t1)
print(t1[0])
# methods of tuple 
# loop through tuple
for i in t1:
    print(i)

# 3)Set: A set is a collection of items that are unordered and unindexed. In Python, sets are written with curly brackets.
s1 = {1, 2, 3, 4, 5}
print(s1)
# methods of set
s1.add(6)
print(s1)
s1.remove(6)
print(s1)
s1.clear()
print(s1)

# loop through set
for i in s1:
    print(i)

# 4)Dictionary: A dictionary is a collection of items that are unordered, changeable and indexed. 
# In Python, dictionaries are written with curly brackets, and they have keys and values.
d1 = {"name": "John", "age": 30, "city": "New York"}
print(d1)
print(d1["name"])
# methods of dictionary
d1["age"] = 31
print(d1)
d1.pop("city")
print(d1)
d1.clear()
print(d1)

# loop through dictionary
for key, value in d1.items():
    print(key, value)
    
# 5)Linked List: A linked list is a linear data structure where each element is a separate object. 
# Each element (node) of a list is comprising of two items - the data and a reference to the next node. 
# The last node has a reference to null. The entry point into a linked list is called the head of the list. 
# If the list is empty then the head is a null reference.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
ll.head.next = second
second.next = third
# loop through linked list
current = ll.head
while current:
    print(current.data)
    current = current.next

# 6)Stack: A stack is a linear data structure that follows the principle of Last In First Out (LIFO).
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) < 1:
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
print(s1.pop())
print(s1.peek())
print(s1.is_empty())
print(s1.size())

# 7)Queue: A queue is a linear data structure that follows the principle of First In First Out (FIFO).
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        return True

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())

# 8)Tree: A tree is a hierarchical data structure that consists of nodes, with a single node called the root, and zero or more child nodes.
#  Each node can have zero or more child nodes, and each child node can have its own child nodes, forming a tree-like structure.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

tr = Tree()
tr.root = Node(1)
tr.root.left = Node(2)
tr.root.right = Node(3)
tr.root.left.left = Node(4)
tr.root.left.right = Node(5)
tr.root.right.left = Node(6)
tr.root.right.right = Node(7)
# loop through tree
current = tr.root
while current:
    print(current.data)
    current = current.left

# 9)Graph: A graph is a non-linear data structure that consists of a finite set of vertices (or nodes)
#  and a set of edges that connect these vertices.
class Graph:
    def __init__(self):
        self.graph = {}
g1 = Graph()
g1.graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
# loop through graph
for key, value in g1.graph.items():
    print(key, value)

# 10)Hash Table: A hash table is a data structure that implements an associative array abstract data type,
#  a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots,
#  from which the desired value can be found.
class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key)

    def remove(self, key):
        if key in self.table:
            del self.table[key]
ht = HashTable()
ht.insert("name", "John")
ht.insert("age", 30)
print(ht.get("name"))
print(ht.get("age"))
ht.remove("age")
print(ht.get("age"))

# 11)Heap: A heap is a specialized tree-based data structure that satisfies the heap property.
class Heap:
    def __init__(self):
        self.heap = []
h1 = Heap()
h1.heap = [1, 2, 3, 4, 5]

    # loop through heap
for i in h1.heap:
    print(i)

# 
