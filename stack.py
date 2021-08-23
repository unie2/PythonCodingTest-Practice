''' Try example of stack structure with Python programming '''

stack = []

stack.append(5) # insert 5
stack.append(2) # insert 2
stack.append(3) # insert 3
stack.append(7) # insert 7

stack.pop() # delete 7

stack.append(1) # insert 1
stack.append(4) # insert 4

stack.pop() # delete 4

print(stack[::-1]) # result => [1, 3, 2, 5]
print(stack) # result => [5, 2, 3, 1]
