# Merging two sorted linked list into a final linked List

from singlyLinkedList import Node , LinkedList

def mergeList(list1 , list2 , result):
    currentFirst = list1.head
    currentSecond = list2.head
    while True:
        if currentFirst is None:
            result.insert(currentSecond)
            break
        if currentSecond is None:
            result.insert(currentFirst)
            break
        if currentFirst.data < currentSecond.data:
            currentFirstNext = currentFirst.next
            currentFirst.next = None
            result.insert(currentFirst)
            currentFirst = currentFirstNext
        else:
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            result.insert(currentSecond)
            currentSecond = currentSecondNext
            
    

if __name__ == "__main__":
    Node1 = Node(1)
    Node2 = Node(3)
    Node3 = Node(4)
    Node4 = Node(2)
    Node5 = Node(7)
    Node6 = Node(9)
    # Inserting nodes in list 1 
    list1 = LinkedList()
    list1.insert(Node1)
    list1.insert(Node2)
    list1.insert(Node3)
    print(" First List ")
    list1.printlist()
    # Inserting nodes in list 2
    list2 = LinkedList()
    list2.insert(Node4)
    list2.insert(Node5)
    list2.insert(Node6)
    print('Second List')
    list2.printlist()
    # Storing the merged list in result 
    result = LinkedList()
    print("The merged List")
    mergeList(list1 , list2 , result)
    result.printlist()
