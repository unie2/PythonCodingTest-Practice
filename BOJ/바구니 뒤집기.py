n, m = map(int, input().split())

data = [i for i in range(n + 1)]

for _ in range(m) :
  i, j = map(int, input().split())
  value = []
  for k in range(i, j + 1) :
    value.append(data[k])
  
  value = value[::-1]
  number = 0
  for k in range(i, j + 1) :
    data[k] = value[number]
    number += 1

for k in range(1, len(data)) :
  print(data[k], end=' ')
  
  
# 1. 입력받은 i부터 j 범위의 data 리스트 값을 value로 따로 뽑아내어 역순으로 순서를 바꾼다.
# 2. 바꾼 value 리스트 값을 하나씩 다시 data 리스트의 해당 범위에 갱신한다.
# 3. 최종적으로 data리스트의 값을 하나씩 출력한다.
