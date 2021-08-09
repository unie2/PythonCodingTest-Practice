''' Using deque from collections Module '''
from collections import deque

data = deque([4, 5, 6])
data.appendleft(3) # Append number 3 to First Index
data.append(7) # Append number 7 to Last Index

print(data)
print(list(data)) # Transform List data type



''' Using Counter from collections Module '''
from collections import Counter

data = Counter(['A', 'B', 'C', 'A', 'C'])

print(data['A']) # Counting 'A'
print(data['B']) # Counting 'B'
print(data['C']) # Counting 'C'

print(dict(data)) # Transform Dictionary data type



