n = int(input())
direction = input().split()

x, y = 1, 1
move = ['L', 'R', 'U', 'D']
gox = [0, 0, -1, 1]
goy = [-1, 1, 0, 0]
for i in direction :
  for j in range(len(move)) :
    if i == move[j] :
      result_x = x + gox[j]
      result_y = y + goy[j]

  if result_x < 1 or result_y < 1 or result_x > n or result_y > n :
    continue

  x = result_x
  y = result_y

print(x, y)
