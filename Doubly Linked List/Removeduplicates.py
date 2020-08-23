from doublylinkedlist import Node, DoublyLinkedList


def removeDuplicates(doublylist1):
    nodeCount = {}
    currentNode = doublylist1.head
    while True:
        if currentNode.data not in nodeCount.keys():
            nodeCount[currentNode.data] = 1
        else:
            nodeCount[currentNode.data] += 1
        if currentNode.next is None:
            while True:
                if currentNode.prev is None:
                    break
                previousNode = currentNode.prev
                if nodeCount[currentNode.data] > 1:
                    currentNode.prev.next = currentNode.next
                    if currentNode.next is not None:
                        currentNode.next.prev = currentNode.prev
                    currentNode.next = None
                    currentNode.prev = None
                    nodeCount[currentNode.data] -=1
                currentNode = previousNode
            break
        currentNode = currentNode.next

if __name__ == "__main__":
    doublylist1 = DoublyLinkedList()
    node1 = Node(13)
    node2 = Node(5)
    node3 = Node(13)
    node4 = Node(2)
    node5 = Node(13)
    doublylist1.insert(node1)
    doublylist1.insert(node2)
    doublylist1.insert(node3)
    doublylist1.insert(node4)
    doublylist1.insert(node5)
    removeDuplicates(doublylist1)
    doublylist1.printlist()