a, b = map(int, input().split())

data = []

for i in range(b+1) :
  for j in range(i) :
    if b == len(data) :
      break
    data.append(i)
  
print(sum(data[a-1:b]))
