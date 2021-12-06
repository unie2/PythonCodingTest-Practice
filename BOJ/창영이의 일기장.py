data = input()
value = ['a', 'e', 'i', 'o', 'u']

number = 0
while number < len(data) :
  print(data[number], end='')
  if data[number] in value :
    number += 2
  number += 1
  
  
# 1. value 리스트에 모음을 정의해놓는다.
# 2. while문을 통해 문자열의 문자를 하나씩 확인하여 화면에 출력한다.
# 3. 조건문을 통해 해당 문자가 value(모음 리스트)에 존재할 경우 인덱스를 의미하는 number 값을 2 증가시킨다.
# 4. 조건문이 끝나면 number값을 1 증가시킨다.
