while True :
  try :
    a, b, c = map(int, input().split())
    result = max(b - a, c - b)
    print(result - 1)
  except :
    break
    
    
# 1. 여러개의 테스트 케이스로 이루어지므로 try ~ except 를 통해 코드를 구성한다.
# 2. a, b, c를 정수형으로 입력받고, 바깥쪽의 캥거루 중 한 마리가 다른 두 캥거루 사이의 정수 좌표로 점프하는데, 최대 몇 번 움직일 수 있는지를 구해야하기 때문에 b-a와 c-b 중 더 큰 값을 result에 할당한다.
# 3. 최종적으로 result에서 1을 뺀 값을 출력한다. 예를 들어, 한 캥거루가 2와 3사이에는 들어갈 수 없기 때문에 0으로 판단해야한다.
