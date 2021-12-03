t = int(input())

for _ in range(t) :
  n = int(input())
  a_score = 0
  b_score = 0

  for _ in range(n) :
    a, b = input().split()
    if a == b :
      continue
    elif (a == 'R' and b == 'S') or (a == 'S' and b == 'P') or (a == 'P' and b == 'R') :
      a_score += 1
    else :
      b_score += 1

  if a_score == b_score :
    print('TIE')
  elif a_score > b_score :
    print('Player 1')
  else :
    print('Player 2')
    
    
# 1. 가위 바위 보를 한 횟수만큼 반복문을 수행하고, 입력받은 a와 b가 같을 경우 넘어간다.
# 2. 입력받은 a가 가위 바위 보 게임에서 승리할 경우 a_score를 1 증가시킨다.
# 3. 입력받은 b가 가위 바위 보 게임에서 승리할 경우 b_score를 1 증가시킨다.
# 4. 반복문이 종료되면 조건문을 통해 a_score와 b_score의 값을 확인한다.
# 5. 만약 a_score와 b_score가 같을 경우 비겼기 때문에 'TIE'를 출력한다.
# 6. 만약 a_score가 b_score보다 클 경우 Player 1이 이겼기 때문에 'Player 1'을 출력한다.
# 7. 만약 b_score가 a_score보다 클 경우 Player 2가 이겼기 때문에 'Player 2'를 출력한다.
