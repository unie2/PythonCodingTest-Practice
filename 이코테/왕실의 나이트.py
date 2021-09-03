n = input()
al = int(ord(n[0])) - int(ord('a')) + 1
number = int(n[1])
result = 0

move = [(-1,2), (1,2), (-2, -1), (-2, 1), (-1,-2), (1, -2), (-1,2), (1, 2)]

for i in move :
  result_row = number + i[0]
  result_column = al + i[1]

  if result_row < 1 or result_column < 1 or result_row > 8 or result_column > 8 :
    continue

  result += 1

print(result)
