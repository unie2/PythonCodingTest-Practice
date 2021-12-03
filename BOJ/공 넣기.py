n, m = map(int, input().split())
data = [0] * n

for _ in range(m) :
  i, j, k = map(int, input().split())
  for i in range(i, j + 1) :
    data[i-1] = k

for i in range(n) :
  print(data[i], end=' ')
  
  
# 1. 반복문을 통해 입력받은 i부터 j+1 (j까지 포함되어야 하기 때문에)까지 범위를 설정하여 data리스트의 값을 k로 갱신한다.
# 2. data리스트는 0부터 시작하고, 문제에서는 1부터 시작하기 때문에 값 갱신 시 data[i-1]를 인덱스로 지정하여 갱신한다.
# 3. 최종적으로 반복문을 통해 리스트에 존재하는 값을 출력한다.
