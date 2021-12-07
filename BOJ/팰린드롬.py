n = input()
value = n[::-1]

if value in n :
  print('true')
else :
  print('false')
  
  
# 1. 입력받은 n을 거꾸로 뒤집어 value에 담는다.
# 2. 조건문을 통해 거꾸로 뒤집혀 있는 value의 값이 n에 존재할 경우 팰린드롬에 해당하기 때문에 'true'를 출력한다.
# 3. 그렇지 않다면 'false'를 출력한다.
