# Sorting the linked list

from singlyLinkedList import Node , LinkedList

def swapNext(llist ,previousNode, largestNode , nextNode):
    largestNode.next = nextNode.next
    nextNode.next = largestNode
    if largestNode is llist.head:
        llist.head = nextNode
        return
    previousNode.next = nextNode
        

def sort(llist):
    numberofiter = llist.listLength() - 1
    while numberofiter != 0:
        largestNode = llist.head
        previousNode = None
        numberofcomparison = numberofiter
        while numberofcomparison !=0:
            if largestNode.data > largestNode.next.data:
                swapNext(llist ,previousNode, largestNode , largestNode.next)
            else:
                previousNode = largestNode
                largestNode = largestNode.next
            #perform this to decrement the comparisons
            numberofcomparison -=1
        # decrement the iterations
        numberofiter -=1
        
if __name__ == "__main__":
    Nodeone = Node(4)
    NodeTwo = Node(3)
    NodeThree = Node(5)
    NodeFour = Node(1)
    llist = LinkedList()
    llist.insert(Nodeone)
    llist.insert(NodeTwo)
    llist.insert(NodeThree)
    llist.insert(NodeFour)
    print('The unsorted List')
    llist.printlist()
    sort(llist)
    print('-----------------')
    print('The sorted List')
    llist.printlist()
    