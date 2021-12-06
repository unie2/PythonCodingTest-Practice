n = int(input())

for _ in range(n) :
  data = list(input().split())
  data[0] = 'god'
  for i in range(len(data)) :
    print(data[i], end='')
  
  print()
  
  
# 1. 문자열을 입력받아 리스트 형태로 구성한다.
# 2. 단순히 data 리스트의 0번째 인덱스 값을 'god'로 갱신한다.
# 3. 반복문을 통해 data 리스트의 값들을 출력형식에 맞추어 출력한다.
