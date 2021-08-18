n = int(input())
x = input().split()
result = []

for i in range(n) :
  x[i] = int(x[i])

for i in range(24) :
  result.append(0)

for i in range(n) :
  result[x[i]] += 1

for i in range(1, 24) :
  print(result[i], end = ' ')
