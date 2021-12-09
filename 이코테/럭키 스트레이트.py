n = input()

number = len(n) // 2

left_value = 0
for i in range(number) :
  left_value += int(n[i])

right_value = 0
for i in range(number, len(n)) :
  right_value += int(n[i])

if left_value == right_value :
  print('LUCKY')
else :
  print('READY')
  
  
# 1. n을 입력받고 n의 길이에 2를 나눈 몫을 number에 할당한다.
# 2. 반복문을 통해 점수 n을 자릿수를 기준으로 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 구한다.
# 3. 조건문을 통해 왼쪽 자릿수의 합과 오른쪽 자릿수의 합이 동일하다면 'LUCKY'를 출력하고 그렇지 않을 경우 'READY'를 출력한다.
