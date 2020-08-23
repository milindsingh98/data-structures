# Stack implementation using lists and pop , push and peek operation

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self , data):
        self.stack.append(data)
        
    def pop(self):
        if self.stack_size() < 1:
            return 'The stack is empty'
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return self.stack == []
    
    def stack_size(self):
        return len(self.stack)
    
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(3)
    stack.push(5)
    print('Size is ' + str(stack.stack_size()))
    print('Popped Item ' + str(stack.pop()))
    print('Popped Item ' + str(stack.pop()))
    print('Popped Item ' + str(stack.pop()))
    print('Popped Item ' + str(stack.pop()))