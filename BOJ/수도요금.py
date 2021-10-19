a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())
value2 = a * p

if p > c :
  value = b + ((p-c) * d)
else :
  value = b

if value > value2 :
  print(value2)
else :
  print(value)
