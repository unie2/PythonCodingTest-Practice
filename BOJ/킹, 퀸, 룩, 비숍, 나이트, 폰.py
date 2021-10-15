c = [1, 1, 2, 2, 2, 8]
data = list(map(int, input().split()))

for i in range(6) :
  print(c[i] - data[i], end=' ')
