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

    def isEmpty(self):
        '''
        Checks whether the linked is empty or not
        '''
        if self.head is None:
            return True
        else:
            return False

    def listLength(self):
        '''
        To display the length of the linked List
        '''
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode =  currentNode.next
        return length
        
        
    def insert_head(self , newNode):
        '''
        Inserts a node at the head/beginning  of the linkedList
        '''
        temp_node = self.head
        self.head = newNode
        self.head.next = temp_node
        del temp_node
        
        
        
    def insert(self , newNode):
        '''
        Inserts a new node at the end of the linkedList
        '''
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
        '''
        Inserts a new node at a given user position
        newNode - Node to add at the position
        position - the positions start with 0, so position should be put accordingly.
        '''
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
        '''
        Inserts a new node between two nodes
        prev_node = Previous Node Data part
        next_node = Next Node Data part
        newNode = New Node that is to be added between the nodes
        '''
        currentNode = self.head
        while True:
            if currentNode.data == prev_node and currentNode.next.data == next_node:
                newNode.next = currentNode.next
                currentNode.next = newNode
                break
            currentNode = currentNode.next

    def insertAfter(self, prev_node, newNode):
        '''
        Inserts a new node after a node
        prev_node = the node after which a new node is to be added
        newNode = New Node that is to be added after a node
        '''
        currentNode = self.head
        while True:
            if currentNode.data == prev_node:
                newNode.next = currentNode.next
                currentNode.next = newNode
                break
            currentNode = currentNode.next
            
    def insertBefore(self, present_node , newNode):
        '''
        Inserts a new node before a node
        present_node = the node before which a new node is to be added
        newNode = New Node that is to be added before a node
        '''
        currentNode = self.head
        previous = None
        while True:
            if currentNode.data == present_node:
                newNode.next = previous.next
                previous.next = newNode
                break
            previous = currentNode
            currentNode = currentNode.next
        
    def delete_end(self):
        '''
        Deletes the node at the end of the linked list
        '''
        if self.isEmpty() is False:
            if self.head.next is None:
                self.delete_head()
                return
            lastNode = self.head
            while lastNode.next is not None:
                previousNode = lastNode
                lastNode = lastNode.next
            previousNode.next = None
            del lastNode
        else:
            print('The list is empty. Delete Failed!')


    def delete_head(self):
        '''
        Deletes the head node of the linkedList
        '''
        if self.isEmpty() is False:
            prevHead = self.head
            self.head = self.head.next
            prevHead.next = None
            del prevHead
        else:
            print('The list is empty. Delete Failed!')
            
    def deleteAt(self , position):
        '''
        Deletes a node at the position passed by user in the function.
        '''
        if position < 0 or position >= self.listLength():
            print('Invalid position')
            return
        if self.isEmpty() is True:
            print('The list is empty')
            return
        elif position == 0:
            self.delete_head()
            return
        else:
            currentNode = self.head
            currentPos = 0
            previousNode = None
            while True:
                if currentPos == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    del currentNode
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                currentPos +=1
                
                
    def delete(self , presentNode):
        '''
        Delets a node by value rather than position. The Node should be passed in the function which is to be deleted
        '''
        if self.isEmpty():
            return
        else:
            currentNode = self.head
            previousNode = None
            while True:
                if currentNode.data == presentNode:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break
                previousNode = currentNode
                currentNode = currentNode.next
            
    def printlist(self):
        '''
        Printing the LinkedList
        '''
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
    linkedList.insert(firstNode) # insert the node at the end pf the list
    secondNode = Node('Kelly')
    linkedList.insert(secondNode)
    thirdNode = Node('Scully')
    linkedList.insert_head(thirdNode) #insert a new node at the head of the linked list
    forthNode = Node('Jake')
    linkedList.insertAtPos(forthNode , 2) #insert a node at position 2
    fifthNode = Node('Charles')
    linkedList.insert_between('John' , 'Jake' , fifthNode) # insert a new node between two nodes
    fifthNode = Node('Amy')
    linkedList.insertAfter('Charles' , fifthNode) #insert a new node after a certain node
    sixthNode = Node('Rosa')
    linkedList.insertBefore('Jake' , sixthNode) #insert a new node before a certain node
    linkedList.delete_head() # delete the head node
    linkedList.printlist()