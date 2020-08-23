from doublylinkedlist import Node , DoublyLinkedList


def palindrome(lis):
    startPointer = lis.head
    endPointer = lis.head
    while endPointer.next is not None:
        endPointer = endPointer.next
    while True:
        if startPointer == endPointer:
            print('List is Palindrone')
            return
        if startPointer.data == endPointer.data:
            startPointer = startPointer.next
            endPointer = endPointer.prev
        else:
            print('List is not Palindrome')
            return

if __name__ == "__main__":
    first = Node('L')
    Second = Node('E')
    Third = Node('V')
    Fourth = Node('E')
    Fifth = Node('L')
    lis = DoublyLinkedList()
    lis.insert(first)
    lis.insert(Second)
    lis.insert(Third)
    lis.insert(Fourth)
    lis.insert(Fifth)
    palindrome(lis)
