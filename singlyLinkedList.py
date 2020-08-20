class Node:
    '''
    The Linked List stores the elements as form of nodes
    Each node contains a data part and a next pointer to point to the next node in the linkedList
    '''
    def __init__(self , data):
        self.data = data
        self.next = None
        
class LinkedList:
    '''
    The LinkedList operations are performed
    The operations are - 
    -inserting at the head / end / between / at certain position
    - Printing List
    '''
    def __init__(self):
        self.head = None
        
        
    def insert_head(self , newNode):
        '''
        Inserts a node at the head/beginning  of the linkedList
        '''
        temp_node = self.head
        self.head = newNode
        self.head.next = temp_node
        del temp_node
        
        
        
    def insert(self , newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
            
    def insertAtPos(self , newNode, position):
        currentNode = self.head
        previousNode = None
        currentPos = 0
        while True:
            if currentPos == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPos +=1
            
    def insert_between(self , prev_node , next_node , newNode):
        currentNode = self.head
        while True:
            if currentNode.data == prev_node and currentNode.next.data == next_node:
                newNode.next = currentNode.next
                currentNode.next = newNode
                break
            currentNode = currentNode.next
        
    
            
    def printlist(self):
        if self.head is None:
            print('List is Empty amigos!')
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
                
            
            
    
if __name__ == '__main__':
    firstNode = Node('John')
    linkedList = LinkedList()
    linkedList.insert(firstNode)
    secondNode = Node('Kelly')
    linkedList.insert(secondNode)
    thirdNode = Node('Scully')
    linkedList.insert_head(thirdNode)
    # linkedList.printlist()

    forthNode = Node('Jake')
    linkedList.insertAtPos(forthNode , 2)
    fifthNode = Node('Charles')
    linkedList.insert_between('John' , 'Jake' , fifthNode)
    linkedList.printlist()