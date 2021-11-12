t = int(input())

for _ in range(t) :
  data = list(map(int, input().split()))
  print(sum(data))
  
  
# 1. 입력받은 테스트 케이스 수만큼 반복하여 한 테스트 케이스가 실행될 때 자연수들을 입력받아 리스트 형태로 구성한다.
# 2. sum( )을 사용하여 data 리스트에 담겨있는 값들의 합을 구하여 출력한다.
