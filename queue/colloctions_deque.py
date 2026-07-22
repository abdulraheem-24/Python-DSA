from collections import deque

queue = deque([1,2,3,4,5,6,7])

queue.append(10)
queue.append(40)
queue.append(50)
queue.appendleft(5)
queue.appendleft(3)
queue.appendleft(20)
queue.insert(4,8)
print(queue.pop())
print(queue.popleft())


print(queue)

