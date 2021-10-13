n, k = map(int, input().split())

data = [True for i in range(n + 1)]
count = 0

for i in range(2, len(data) + 1) :
  for j in range(i, n+1, i) :
    if data[j] :
      data[j] = False
      count += 1
      if count == k :
        print(j)
        break
