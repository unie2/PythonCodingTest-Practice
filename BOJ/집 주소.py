while True :
  n = input()
  if int(n) == 0 :
    break
  sum_value = 2 + int(len(n)) - 1
  for i in range(len(n)) :
    if int(n[i]) == 1 :
      sum_value += 2
    elif int(n[i]) == 0 :
      sum_value += 4
    else :
      sum_value += 3

  print(sum_value)
  
  
# 1. while문을 통해 입력받은 수(n)가 0일때까지 반복 수행한다.
# 2. sum_value에 오른쪽, 왼쪽 경계의 여백(총 2cm)과 각 숫자 사이의 여백(1cm씩)을 더하여 담는다.
# 3. 반복문을 통해 입력받은 n의 수를 한 문자씩 확인하여 정수형으로 변환하여 조건문을 수행한다.
# 4. 만약 현재 값이 1일 경우 2cm의 너비를 차지하기 때문에 sum_value에 2를 누적한다.
# 5. 만약 현재 값이 0일 경우 4cm의 너비를 차지하기 때문에 sum_value에 4를 누적한다.
# 6. 나머지 숫자는 모두 3cm의 너비를 차지하기 때문에 sum_value에 3을 누적한다.
