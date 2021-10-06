data = []
for _ in range(5) :
  n = int(input())
  if n < 40 :
    data.append(40)
  else :
    data.append(n)

print(sum(data) // 5)
