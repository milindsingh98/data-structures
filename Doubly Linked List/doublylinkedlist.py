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
        self.head.next = tempNode
        tempNode.prev = self.head
        del tempNode
        
    
    def insertAt(self , newNode , position):
        if self.isEmpty() or self.listlength() < 0 or self.listlength() <= position:
            print('The list either empty or the position is more than listlength')
            return
        if position is 0:
            self.insert_head(newNode)
            return
        if position is self.listlength():
            self.insert(newNode)
            return
        else:
            currentNode = self.head
            currentPos = 1
            while True:
                if currentPos == position:
                    currentNode.prev.next = newNode
                    newNode.prev = currentNode.prev
                    newNode.next = currentNode
                    currentNode.prev = newNode
                    break
                currentPos +=1
                currentNode = currentNode.next
            
    
    def insert_before(self , newNode, markedNode):
        if self.isEmpty():
            print('The list is empty')
            return
        else:
            currentNode = self.head
            while True:
                if currentNode.data == markedNode:
                    currentNode.prev.next = newNode
                    newNode.prev = currentNode.prev
                    newNode.next = currentNode
                    currentNode.prev = newNode
                    break
                currentNode = currentNode.next
    
    def insert_after(self, newNode, markedNode):
        if self.isEmpty():
            print('The list is empty')
            return
        currentNode = self.head
        while True:
            if currentNode.data == markedNode:
                nextNode = currentNode.next #marking the next Node to currentNode
                currentNode.next = newNode 
                newNode.prev = currentNode
                newNode.next = nextNode
                nextNode.prev = newNode
                break
            currentNode = currentNode.next
            
    
        
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
            newNode.prev = currentNode

    def deleteNode(self , markedNode):
        if self.isEmpty():
            print('The list is empty')
            return
        currentNode = self.head
        previousNode = None
        while True:
            if currentNode.data == markedNode:
                tempNode = currentNode
                previousNode.next = currentNode.next
                currentNode.next.prev = previousNode
                del tempNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            
    def delete_head(self):
        tempNode = self.head
        self.head = tempNode.next
        self.head.prev = None
        del tempNode
        
            
    def deleteAt(self , position):
        if self.isEmpty() or self.listlength()<0:
            print('The linkedList is empty')
            return
        if position == 1:
            self.delete_head()
            return
        currentNode = self.head
        currentPos = 1
        while True:
            if currentPos == position:
                tempNode = currentNode
                currentNode.prev.next = currentNode.next
                currentNode.next.prev = currentNode.prev
                del tempNode
                break
            currentPos +=1
            currentNode = currentNode.next
            
    def deleteEnd(self):
        if self.isEmpty() or self.listlength() <= 0:
            print('THe linkedList is empty')
            return
        if self.listlength() == 1:
            self.delete_head()
            return
        lastNode = self.head
        while True:
            if lastNode.next.next is None:
                lastNode.next.prev = None
                lastNode.next.next = None
                lastNode.next = None
                break
            lastNode = lastNode.next
            
    def printlist(self):
        if self.head is None:
            print('The list is None')
            return
        else:
            currentNode = self.head
            print('Printing from the beginning')
            while True:
                if currentNode is None:
                    break
                print(currentNode.data)
                if currentNode.next is None:
                    reverseNode = currentNode
                currentNode = currentNode.next
            print('Printing from the end')
            while True:
                if reverseNode is None:
                    break
                print(reverseNode.data)
                reverseNode = reverseNode.prev
                
            
                
if __name__ == "__main__":          
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
    SixthNode = Node('Holt')
    doublylist.insert_after(SixthNode , 'Rosa')
    doublylist.deleteNode('Holt')
    doublylist.delete_head()
    doublylist.deleteAt(2)
    doublylist.deleteEnd()
    doublylist.printlist()
