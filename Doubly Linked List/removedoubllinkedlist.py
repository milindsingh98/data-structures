#Importing the classes LinkedList and Node from the DoublyLinkedlist.py

from doublylinkedlist import Node, DoublyLinkedList

def reverseList(doublylist):
    currentNode = doublylist.head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = currentNode.prev
        currentNode.prev = nextNode
        if currentNode.prev is None:
            doublylist.head = currentNode
        currentNode = nextNode
    

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
    reverseList(doublylist)
    doublylist.printlist()