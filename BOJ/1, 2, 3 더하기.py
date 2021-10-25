tc = int(input())
data = [1, 2, 4]

for i in range(3, 10) :
  data.append(data[i-1] + data[i-2] + data[i-3])

for i in range(tc) :
  n = int(input())
  print(data[n-1])
