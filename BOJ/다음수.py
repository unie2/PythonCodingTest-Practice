while True :
  a, b, c = map(int, input().split())
  if a == 0 and b == 0 and c == 0 :
    break
  
  if b - a == c - b :
    print(f"AP {c + (c-b)}")
  else :
    print(f"GP {c * (c // b)}")
    
    
# 1. while문을 통해 입력받은 세 수가 모두 0일때까지 반복 수행한다.
# 2. 조건문을 통해 두번째 수와 첫번째 수의 차와 세번째 수와 두번째 수의 차가 같을 경우 등차수열에 해당한다.
# 3. 그렇지 않을 경우 등비수열에 해당해 문제에서 요구하는 출력형식에 맞추어 값을 출력한다.
