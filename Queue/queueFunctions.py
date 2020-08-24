# queue created with the help of the python inbuilt lists
# The time complexity of each case in the best case scenario is O(1)
# Time complexity in the worst case scenario is O(n)
# The functions included are - Enqueue , - Dequeue -isEmpty , -peek


class Queue:
    def  __init__(self):
        '''
        initializing the queue
        '''
        self.queue = []
        
    def isEmpty(self):
        '''
        to check whether the queue is empty or not
        '''
        return self.queue == []
    
    def enqueue(self ,data):
        '''
        to add the data into the queue
        '''
        self.queue.append(data)
        
    def dequeue(self):
        '''
        to remove the first elemt from the the queue.
        The queue follows FIFO
        '''
        if self.queue_size() < 1:
            return 'The queue is empty'
        data = self.queue[0]
        del self.queue[0]
        return data
        
    def peek(self):
        '''
        returns the  first element of the queue
        '''
        return self.queue[0]
    
    def queue_size(self):
        '''
        returns the size of the the queue
        '''
        return len(self.queue)
    
    
q = Queue()
q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
print('The first value is ' , q.dequeue() )
print('The first value is ' , q.dequeue() )
print('The first value is ' , q.dequeue() )
print('The first value is ' , q.dequeue() )
print('The first value is ' , q.dequeue() )