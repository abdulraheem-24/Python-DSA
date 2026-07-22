# list implementation 

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

item = stack.pop()

print(item)
print(stack)

#isEmpty
print(len(stack) == 0)




# linkedlist implementation


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_data = Node(data)
        new_data.next = self.top
        self.top = new_data
    

    def pop(self):
        if self.top == None:
            return None
        
        
        data = self.top.data
        self.top = self.top.next
        return data


    def display(self):
        current = self.top
        while current:
            print(current.data, end="->")
            current = current.next
        print(current)

    def isEmpty(self):
        return self.top is None

    def peek(self):
        if self.top:
            return self.top.data
        return None
    

s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)

s.display()


print(s.pop())
s.display()