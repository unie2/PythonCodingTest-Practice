t = int(input())

for _ in range(t) :
  value = list(map(int, input().split()))
  data = []
  for i in range(len(value)) :
    if value[i] % 2 == 0 :
      data.append(value[i])

  print(sum(data), min(data))
