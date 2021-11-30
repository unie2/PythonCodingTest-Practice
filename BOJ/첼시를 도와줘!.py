n = int(input())

for _ in range(n) :
  p = int(input())
  max_price = 0
  max_name = ""
  for _ in range(p) :
    c, name = input().split()
    if int(c) > max_price :
      max_price = int(c)
      max_name = name
  
  print(max_name)
  
  
# 1. 입력받은 값들 중 가장 비싼 선수를 찾아내기 위해 max_price와 max_name을 초기화한다.
# 2. 입력받은 선수의 가격이 max_price보다 클 경우 max_price을 입력받은 선수의 가격으로 갱신하고 max_name을 입력받은 선수의 이름으로 갱신한다.
# 3. 내부 반복문이 종료되면 최종적으로 max_name을 출력한다.
