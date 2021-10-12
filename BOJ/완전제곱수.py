import math

m = int(input())
n = int(input())
result = []

for i in range(m, n + 1) :
  if int(math.sqrt(i)) ** 2 == i :
    result.append(i)

if result :
  print(sum(result))
  print(min(result))
else :
  print(-1)
