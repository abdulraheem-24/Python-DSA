# linked list implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_data = Node(data)

        if self.front == None:
            self.front = self.rear = new_data
            return
        
        self.rear.next = new_data
        self.rear = new_data
    
    def dequeue(self):
        if self.front == None:
            return None
        
        data = self.front.data
        self.front = self.front.next

        if self.front == None:
            self.rear = None
        
        return data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print(current)

    def front(self):
        if self.front:
            return self.front.data
        return None
    
q = Queue()


q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.dequeue()

q.display()

