# Removing duplicates from the sorted linkedList

from singlyLinkedList import Node, LinkedList

def Remove_Duplicates(linkedlist):
    currentNode = newlist.head
    previousNode = None
    while currentNode !=None:
        if currentNode.data == currentNode.next.data:
            tempNode = currentNode
            previousNode.next = tempNode.next
            tempNode.next = None
            del tempNode
        previousNode = currentNode
        currentNode = currentNode.next

if __name__ == "__main__":
    n1 = Node(3)
    n2 = Node(5)
    n3 = Node(5)
    n4 = Node(8)
    n5 = Node(10)
    newlist = LinkedList()
    newlist.insert(n1)
    newlist.insert(n2)
    newlist.insert(n3)
    newlist.insert(n4)
    newlist.insert(n5)
    Remove_Duplicates(newlist)
    newlist.printlist()