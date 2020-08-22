# Swapping the two nodes of the linkedList

from singlyLinkedList import Node , LinkedList

def swapNode(newlist , dataOne, dataTwo):
    currentNode = newlist.head
    FirstNode = None
    SecondNode = None
    previousFirst = None
    previousSecond = None
    # Disconnecting the link of first node
    while True:
        if currentNode.data == dataOne:
            previousFirst.next = currentNode.next
            currentNode.next = None
            FirstNode = currentNode
            break
        previousFirst = currentNode
        currentNode = currentNode.next
    currentNode = newlist.head
    # Disconnecting the link of the second node
    while True:
        if currentNode.data == dataTwo:
            previousSecond.next = currentNode.next
            currentNode.next = None
            SecondNode = currentNode
            break
        previousSecond = currentNode
        currentNode = currentNode.next
    
    #Reconnecting the nodes and swapping their positions
    SecondNode.next = previousFirst.next
    previousFirst.next = SecondNode
    FirstNode.next = previousSecond.next
    previousSecond.next = FirstNode
        

if __name__ == "__main__":
    n1 = Node(3)
    n2 = Node(5)
    n3 = Node(7)
    n4 = Node(8)
    n5 = Node(10)
    newlist = LinkedList()
    newlist.insert(n1)
    newlist.insert(n2)
    newlist.insert(n3)
    newlist.insert(n4)
    newlist.insert(n5)
    print('The original List')
    newlist.printlist()
    print('\n-------------------------------------\n')
    print('Swapping the nodes 5 and 8')
    swapNode(newlist , 5 , 8)
    print('The linked list with swapped nodes')
    newlist.printlist()
