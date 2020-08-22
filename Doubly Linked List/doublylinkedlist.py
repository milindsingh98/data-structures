class Node:
    def __init__(self ,data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def listlength(self):
        if self.isEmpty():
            print('The list is empty')
            return
        else:
            currentNode = self.head
            length = 0
            while currentNode is not None:
                length += 1
                currentNode = currentNode.next
            return length
        
    def insert_head(self , newNode):
        tempNode = self.head
        self.head = newNode
        newNode.next = tempNode
        newNode.prev = None
        del tempNode
        
    
    def insertAt(self , newNode , position):
        if self.isEmpty() or self.listlength() < 0 or self.listlength() <= position:
            print('The list either empty or the position is more than listlength')
            return
        else:
            currentNode = self.head
            currentPos = 1
            while True:
                if currentPos == position:
                    newNode.next = currentNode.next
                    currentNode.next = newNode
                    newNode.prev = currentNode.next
                    break
                currentPos +=1
                currentNode = currentNode.next
            
    
    def insert_before(self , newNode, markedNode):
        if self.isEmpty():
            print('The list is empty')
            return
        else:
            currentNode = self.head
            previousNode = None
            while True:
                if currentNode.data is markedNode:
                    newNode.next = previousNode.next
                    previousNode.next = newNode
                    currentNode.prev = newNode.next
                    break
                previousNode = currentNode
                currentNode = currentNode.next
    
    def insert_after(self, newNode, markedNode):
        pass
    
        
    def insert(self , newNode):
        if self.head is None:
            self.head = newNode
            return
        else:
            currentNode = self.head
            while True:
                if currentNode.next is None:
                    break
                currentNode = currentNode.next
            currentNode.next = newNode
            newNode.prev = currentNode.next
            
    def printlist(self):
        if self.head is None:
            print('The list is None')
            return
        else:
            currentNode = self.head
            while True:
                if currentNode is None:
                    break
                print(currentNode.data)
                currentNode = currentNode.next
            
FirstNode = Node('Norm')
SecondNode = Node('Scully')
doublylist = DoublyLinkedList()
doublylist.insert(FirstNode)
doublylist.insert(SecondNode)
ThirdNode = Node('Jake')
doublylist.insert_head(ThirdNode)
FourthNode = Node('Rosa')
doublylist.insertAt(FourthNode , 2)
FifthNode = Node('Amy')
doublylist.insert_before(FifthNode , 'Rosa')
doublylist.printlist()