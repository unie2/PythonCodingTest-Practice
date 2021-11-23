list_value = list(map(int, input().split()))
list_value.sort()
a = list_value[0]
b = list_value[1]
c = list_value[2]

data = input()

for i in range(len(data)) :
  if data[i] == 'A' :
    print(a, end=' ')
  elif data[i] == 'B' :
    print(b, end=' ')
  else :
    print(c, end=' ')
    
    
# 1. 세 수를 리스트 형태로 구성하여 입력받아 오름차순으로 정렬한다.
# 2. 오름차순으로 정렬된 리스트의 0번째 인덱스 값을 a에 할당하고, 1번째 인덱스 값을 b에 할당하고 2번째 인덱스 값을 c에 할당한다.
# 3. 반복문을 통해 입력받은 문자열의 문자를 하나씩 확인하고 조건문을 통해 현재 확인하고 있는 값이 A일 경우 a를 출력한다.
# 4. 현재 확인하고 있는 값이 B일 경우 b를 출력하고, C일 경우 c를 출력한다.
