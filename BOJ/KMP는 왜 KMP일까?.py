data = list(map(str, input().split("-")))

for i in range(len(data)) :
  for j in range(1) :
    print(data[i][j], end='')
    
    
# 입력받는 문자열을 하이픈('-')으로 구분하여 data리스트에 담고, 이중 for문을 통해 i번째 행의 첫번째 문자를 출력한다.
