l, p = map(int, input().split())
data = list(map(int, input().split()))
value = l * p

for i in range(len(data)) :
  print(data[i] - value, end = ' ')
