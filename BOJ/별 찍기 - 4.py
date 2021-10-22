n = int(input())
area = 0

for i in range(n, 0, -1) :
  print(" " * area + "*" * i)
  area += 1
