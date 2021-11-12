for _ in range(3) :
  t = int(input())
  data = []
  for _ in range(t) :
    data.append(int(input()))
  
  if sum(data) == 0 :
    print(0)
  elif sum(data) > 0 :
    print("+")
  else :
    print("-")
    
    
# 1. 각 테스트 셋에서 t개의 정수를 입력받기 위한 t를 입력받는다.
# 2. t개의 정수를 입력받아 data 리스트에 추가한다.
# 3. 조건문을 통해 data리스트에 담겨 있는 값들의 합이 0이라면 0을 출력한다.
# 4. data리스트에 담겨 있는 값들의 합이 0보다 크다면 "+"를 출력한다.
# 5. data리스트에 담겨 있는 값들의 합이 0보다 작다면 "-"를 출력한다.
