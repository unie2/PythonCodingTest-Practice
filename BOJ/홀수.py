data = [0] * 8
h = []
for i in range(7) :
  data[i] = int(input())
  if data[i] % 2 != 0 :
    h.append(data[i])

if h :
  h.sort()
  print(sum(h))
  print(h[0])
else :
  print(-1)
