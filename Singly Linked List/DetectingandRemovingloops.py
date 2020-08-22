# detecting and removing the circular links from the linkedList
# Importing the classes from the singlyLinkedList.py

from singlyLinkedList import Node, LinkedList

#inherit the Node class and add isVisited to the inherited class

class NewNode(Node):
    def __init__(self ,data):
        super().__init__(data)
        self.isvisited = False

#Since it is ouut the of the classes now so we will pass the linked list 
#in teh fucntion parameters

def detectCycle(linkedlist):
    currentNode = linkedlist.head
    currentNode.isvisited = True
    while True:
        if currentNode.next.isvisited is True:
            currentNode.next = None
            break
        currentNode = currentNode.next
        currentNode.isvisited = True

if __name__ == '__main__':
    node1 = NewNode('Scully')
    node2 = NewNode('Rosa')
    node3 = NewNode('Hitchcock')
    linkedlist = LinkedList()
    linkedlist.insert(node1)
    linkedlist.insert(node2)
    linkedlist.insert(node3)
    node3.next = node2
    detectCycle(linkedlist)
    linkedlist.printlist()