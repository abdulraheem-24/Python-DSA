class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
    def display (self) :
        print(self.next)

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3

n1.display()

for n in [n1,n2,n3] :
    print(n.data)
    print(n.next.data if n.next != None else n.next)