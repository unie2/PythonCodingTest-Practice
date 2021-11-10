while True :
  a, b = map(int, input().split())
  if a == 0 and b == 0 :
    break
  d = a // b
  print(f"{d} {a - (d*b)} / {b}")
  
  
# 1. while문을 통해 입력받은 두 수가 모두 0일때까지 반복 수행한다.
# 2. 대분수를 의미하는 d에 입력받은 a를 b로 나눈 몫을 할당한다.
# 3. 출력 형식에 맞추어서 문제에서 요구하는 값을 출력한다.
