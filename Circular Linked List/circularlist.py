class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self , newNode):
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return
        currentNode = self.head
        while currentNode.next is not self.head:
            currentNode = currentNode.next
        currentNode.next = newNode
        newNode.next = self.head
        
    def insert_head(self, newNode):
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return
        lastNode = self.head
        while lastNode.next is not self.head:
            lastNode = lastNode.next
        newNode.next = self.head
        self.head = newNode
        lastNode.next = newNode
        
    def delete(self):
        lastNode = self.head
        while lastNode.next is not self.head:
            previousNode = lastNode
            lastNode = lastNode.next
        lastNode.next = None
        previousNode.next = self.head
        
    def delete_head(self):
        lastNode = self.head
        while lastNode.next is not self.head:
            lastNode = lastNode.next
        previousHead = self.head
        self.head = self.head.next
        lastNode.next = self.head
        previousHead.next = None
        
    def printlist(self):
        if self.head is None:
            print('List is empty')
            return
        currentNode = self.head
        while True:
            print(currentNode.data)
            if currentNode.next is self.head:
                break
            currentNode = currentNode.next
            
        currentNode = currentNode.next
        print(currentNode.data)
        
    
nodeOne = Node('Jake')
nodeTwo = Node('Amy')
nodeThree = Node('Rosa')
nodeFour = Node('Terry')
nodeFive = Node('Scully')
linkedlist = CircularLinkedList()
linkedlist.insert(nodeOne)
linkedlist.insert(nodeTwo)
linkedlist.insert(nodeThree)
linkedlist.insert(nodeFour)
linkedlist.insert_head(nodeFive)
linkedlist.delete()
linkedlist.delete_head()
linkedlist.printlist()
