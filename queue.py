''' Trying Queue structure example using the deque library '''

from collections import deque

# Using deque library for Queue
queue = deque()

queue.append(5) # insert 5
queue.append(2) # insert 2
queue.append(3) # insert 3
queue.append(7) # insert 7

queue.popleft() # delete 5

queue.append(1) # insert 1
queue.append(4) # insert 4

queue.popleft() # delete 2

print(queue) # result => deque([3, 7, 1, 4])
queue.reverse()
print(queue) # result => deque([4, 1, 7, 3])
