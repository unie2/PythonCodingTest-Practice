p = []

for i in range(20) :
  p.append([])
  for j in range(20) :
    p[i].append(0)

n = int(input())
for i in range(n) :
  x, y = map(int, input().split())
  p[x][y] = 1

for i in range(1, 20) :
  for j in range(1, 20) :
    print(p[i][j], end = ' ')
  print()
