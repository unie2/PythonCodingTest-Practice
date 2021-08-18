p = [[] * 10 for _ in range(10)]

for i in range(10) :
  p[i] = list(map(int, input().split()))

x = 1
y = 1
p[x][y] = 9

while(1) :
  if p[x][y] == 2 :
    p[x][y] = 9
    break
  if p[x][y+1] != 1 :
    p[x][y] = 9
    y += 1
  else :
    if p[x+1][y] != 1 :
      p[x][y] = 9
      x += 1
    else :
      p[x][y] = 9
      break


for i in range(10) :
  for j in range(10) :
    print(p[i][j], end = ' ')
  print()
