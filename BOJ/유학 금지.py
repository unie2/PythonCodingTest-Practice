data = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

value = input()
for i in range(len(value)) :
  if value[i] not in data :
    print(value[i], end='')
    
    
# 1. 문제에서 CAMBRIDGE에 포함된 알파벳은 모두 지우기로 했으므로 data 리스트에 해당 알파벳들을 할당해놓는다.
# 2. 반복문을 통해 입력받은 문자열의 문자들을 하나씩 확인한다.
# 3. 조건문을 통해 현재 확인하고 있는 문자가 data 리스트에 존재하지 않을 경우 해당 알파벳을 출력한다.
