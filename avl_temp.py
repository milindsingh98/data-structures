class Node:
    def __init__(self , data , parent):
        self.data = data
        self.parent = parent
        self.leftChild = None
        self.rightChild = None
        self.height = 0

class AVL:
    def __init__(self):
        self.root = None

    def insert(self , data):
        if self.root is None:
            self.root = Node(data , None)
        else:
            self.insert_node(self , data , self.root)

    def insert_node(self, data , node):
        #checking the left subtree
        if node.data < data:
            if node.leftChild:
                self.insert_node(node.leftChild)
            else:
                node.leftChild = Node(data , node)
                node.height = max(self.calculate_height(node.leftChild) ,
                                self.calculate_height(node.rightChild)) +1
        if node.data < data:
            if node.rightChild:
                self.insert_node(data , node.rightChild)
            else:
                node.rightChild = Node(data , node)
                node.height = max(self.calculate_height(node.leftChild) ,
                                self.calculate_height(node.rightChild)) +1

        self.handle_violation(node)

    def calculate_height(self , node):
        

        