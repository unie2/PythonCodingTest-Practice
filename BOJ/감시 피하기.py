
    board[x][y] = 'O'
  # 학생이 한 명도 감지되지 않는 경우
  if not process() :
    find = True
    break
  
  # 설치된 장애물을 다시 없애기
  for x, y in data :
    board[x][y] = 'X'

if find :
  print('YES')
else :
  print('NO')
