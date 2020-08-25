# Binary Search trees - The implementation of the various insertion , deletion  of the nodes of the trees.
# The time complexity of each operation is O(log n) in case of the trees being balanced and the worst case scenario can be considered
# when the tree is unbalanced and the linear time complexity is achieved that is O(n). 

class Node:
    def __init__(self, data , parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self , data):
        if self.root is None:
            self.root = Node(data , None)
        else:
            self.insert_node(data , self.root)

    def insert_node(self , data , node):
        #check the left subtree
        if data < node.data:
            if node.leftChild:
                self.insert_node(data , node.leftChild)
            else:
                node.leftChild = Node(data , node)
        #Check the right subtree
        else:
            if node.rightChild:
                self.insert_node(data , node.rightChild)
            else:
                node.rightChild = Node(data , node)

    def traverse(self):
        if self.root is not None:
           self.traverse_in_order(self.root)

    def traverse_in_order(self , node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)

        print(node.data)

        if node.rightChild:
            self.traverse_in_order(node.rightChild)

    def remove(self , data):
        if self.root:
            self.remove_node(data , self.root)
        
    def remove_node(self , data , node ):
        if node is None:
            return

        if data < node.data:
            self.remove_node(data , node.leftChild)
        elif data > node.data:
            self.remove_node(data , node.rightChild)
        else:
            if node.leftChild is None and node.rightChild is None:
                print('Deleting the leaf node....')

                parent = node.parent

                if parent is not None and parent.leftChild == node:
                    parent.leftChild = None
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = None

                if parent is None:
                    self.root = None

                del node

            elif node.leftChild is None and node.rightChild is not None:
                print('Removing the right child node with single child...')

                parent = node.parent 

                if parent is not None:
                    if node.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                else:
                    self.rote = node.rightChild

                node.rightChild.parent = parent
                del node

            elif node.leftChild is not None and node.rightChild is None:
                print('Removing the node with the single left child')

                parent = node.parent
                if parent is not None:
                    if node.leftChild == node:
                        parent.leftChild = node.leftChild
                    if node.rightChild == node:
                        parent.rightChild = node.leftChild

                else:
                    self.root = node.leftChild

                node.leftChild.parent = parent
                del node

            else:
                print('Removing the root node')

                predecessor = self.get_predecessor(node.leftChild)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data , predecessor)

    def get_predecessor(self , node):
        if node.rightChild:
            self.get_predecessor(node.rightChild)
        return node

    def getMax(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self , node):
        if node.rightChild:
            return self.get_max(node.rightChild)
        return node.data

    def getMin(self):
        if self.root:
            return self.get_min(self.root)
        
    def get_min(self , node):
        if node.leftChild:
            return self.get_min(node.leftChild)
        return node.data


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(5)
    bst.insert(43)
    bst.insert(-5)
    bst.insert(66)
    bst.insert(72)
    bst.remove(43)
    bst.traverse()
    print(bst.getMax())
    print(bst.getMin())


                