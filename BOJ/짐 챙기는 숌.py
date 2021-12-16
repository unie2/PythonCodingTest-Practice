n, m = map(int, input().split())
if n == 0 :
  print(0)
else :
  data = list(map(int, input().split()))

  target = 0
  result = 1
  for i in range(n-1, -1, -1) :
    target += data[i]
    if target > m :
      result += 1
      target = data[i]

  print(result)
  
  
# 1. 입력받은 책의 개수(n)가 0이라면 박스가 아예 필요없으므로 0을 출력한다.
# 2. 그렇지 않을 경우 n개의 책의 무게를 입력받아 리스트 형태로 구성한다.
# 3. 책이 쌓여져 있으므로 리스트에 저장된 값을 거꾸로 하나씩 확인하여 반복문을 수행한다.
# 4. data 리스트 내 현재 확인하고 있는 값을 target에 누적한다.
# 5. 조건문을 통해 target의 값이 입력받은 박스 최대 무게(m)보다 클 경우 result를 1증가시키고 target 값을 현재 확인하고 있는 값으로 갱신한다.
# 6. 반복문이 종료되면 최종적으로 result 값을 출력한다.
