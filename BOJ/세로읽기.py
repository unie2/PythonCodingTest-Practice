data = [[0]*15 for i in range(5)]

for i in range(5) :
  s = list(input())
  for j in range(len(s)) :
    data[i][j] = s[j]

for i in range(15) :
  for j in range(5) :
    if data[j][i] != 0 :
      print(data[j][i], end='')
    else :
      continue
      
      
# 1. 5행 15열 리스트 형태를 구성하여 선언한다.
# 2. 반복문을 통해 각 행에 대한 열에 할당할 문자열을 입력받아 해당 값으로 하나씩 리스트 값을 갱신한다.
# 3. 반복문을 통해 세로로 값을 하나씩 확인하여 그 값이 0이 아닌 경우 출력하고 0일 경우 다음 인덱스 값으로 넘어간다.
