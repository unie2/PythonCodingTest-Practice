n = int(input())

for i in range(1, n + 1) :
  data = list(map(int, input().split()))
  max_value = max(data) ** 2
  data.remove(max(data))

  print('Scenario #'+str(i)+':')
  if data[0]**2 + data[1]**2 == max_value :
    print('yes')
  else :
    print('no')
  print()
  
  
# 1. 각 테스트 케이스마다 세 정수를 입력받아 리스트 형태로 구성한다.
# 2. max_value에 data 리스트에 담겨있는 최댓값의 제곱값을 담고 그 최댓값을 리스트에서 제거한다.
# 3. 조건문을 통해 data리스트에 담겨 있는 나머지 두개의 각 제곱값의 합이 max_value와 같을 경우 
# 직각삼각형 조건에 만족하기 때문에 'yes'를 출력하고 그렇지 않다면 'no'를 출력한다.
# 4. 각 테스트 케이스 사이에 빈 줄을 하나 출력해야 하기 때문에 하나의 테스트케이스가 끝날 무렵 줄바꿈 처리를 한다.
