class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
    
    def display(self):
        current = self.head

        while current:
            print(current.data, end="->")
            current = current.next
        
        print(current)
    
    def insertion_bigenning(self, data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data
    
    def insertion_end(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
            return

        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_data

    def insert_at_position(self, index, data):
        if index == 0:
            self.insertion_bigenning(data)
            return

        new_data = Node(data)
        current = self.head
        for _ in range(index - 1):
            if current.next == None:
                break
            current = current.next

        
        new_data.next = current.next
        current.next = new_data
    
    def delete_start(self):
        self.head = self.head.next
    
    def delete_end(self):
        current = self.head
        while current:
            if current.next.next == None:
                break
            current = current.next
        current.next = None
    
    def delete_position(self, index):
        if index == 0:
            self.delete_start()
            return
        current = self.head
        for _ in range(index - 1):
            if current.next.next == None:
                break
            current = current.next
        
        current.next = current.next.next

    def search_value(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

li = Linked_list()

li.head = Node(10)
li.head.next = Node(20)
li.head.next.next = Node(30)

li.display()
li.insertion_bigenning(40)
li.insertion_end(50)
li.insert_at_position(3, 100)
li.display()



li.delete_start()
li.delete_end()
li.delete_position(10)
li.display()


print(li.search_value(20))