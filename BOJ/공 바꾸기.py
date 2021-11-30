n, m = map(int, input().split())
data = [i for i in range(1, n + 1)]

for _ in range(m) :
  i, j = map(int, input().split())
  temp = data[i-1]
  data[i-1] = data[j-1]
  data[j-1] = temp

for x in range(len(data)) :
  print(data[x], end=' ')
  
  

# 1. 입력받은 n개의 바구니만큼 data 리스트를 생성한다.
# 2. i와 j를 입력받고 temp를 통해 두 바구니에 들어있는 공을 교환한다.
# 3. 반복문을 통해 data 리스트에 존재하는 값을 출력한다.
