t = int(input())

for _ in range(t) :
  n = int(input())
  data = list(input().split())
  
  for _ in range(n - 1) :
    a, b = input().split()
    if int(data[1]) < int(b) :
      data[0] = a
      data[1] = b
  
  print(data[0])
  
  
# 1. 입력받은 n만큼 반복문을 수행하기 전에 첫 입력값을 먼저 리스트 형태로 구성한다.
# 2. 값을 한번 입력받았기 때문에 반복문 횟수는 n - 1로 설정하여 수행한다.
# 3. 학교(a)와 지난 한 해동안 소비한 술의 양(b)을 입력받아 리스트에 담겨 있는 값과 비교하여 더 큰 값으로 갱신한다.
# 4. 최종적으로 data 리스트의 값은 입력받은 값 중 최대값이 담겨 있으므로 학교명(data[0])을 출력한다.
