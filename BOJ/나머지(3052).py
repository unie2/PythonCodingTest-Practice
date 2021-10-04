data = []
for i in range(10) :
  n = int(input())
  data.append(n % 42)

data = set(data)
print(len(data))
