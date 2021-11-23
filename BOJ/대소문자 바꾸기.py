data = input()

for i in range(len(data)) :
  if 65 <= ord(data[i]) <= 90 :
    print(chr(ord(data[i])+32), end='')
  else :
    print(chr(ord(data[i])-32), end='')
    
    
# 1. 반복문을 통해 입력받은 문자열에서 문자들을 하나씩 확인한다.
# 2. 조건문을 통해 현재 확인하고 있는 문자가 대문자일 경우 아스키코드 값으로 변환하여 32를 더해 소문자로 출력한다.
# 3. 현재 확인하고 있는 문자가 소문자일 경우 아스키코드 값으로 변환하여 32를 빼 대문자로 출력한다.
