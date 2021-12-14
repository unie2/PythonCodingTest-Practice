board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board :
  print(-1)
else :
  print(board)
  
  
# 1. 단순히 문자를 치환하는 문제로, 문자열 board에서 'XXXX'가 있다면 'AAAA'로 갱신한다.
# 2. 문자열 board에서 'XX'가 있다면 'BB'로 갱신한다.
# 3. 최종적으로 문자열 board를 확인하여 문자 'X'가 존재할 경우 펄리오미노로 덮을 수 없으므로 -1을 출력한다.
# 4. 'X'가 존재하지 않을 경우 문자열 board를 출력한다.
