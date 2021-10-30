n = int(input())

data = [0] * 81
data[0] = 4
data[1] = 6

for i in range(2, n + 1) :
  data[i] = data[i-1] + data[i-2]

print(data[n-1])
