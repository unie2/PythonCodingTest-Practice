t = int(input())

for _ in range(t) :
  n, data = input().split()
  n = int(n)
  print(data[:n-1], data[n:], sep='')
  
  
# 1. 오타를 낸 위치를 의미하는 n과 문자열을 의미하는 data를 입력받아 n은 정수형으로 변환한다.
# 2. 출력 시 처음부터 n-1까지의 범위와 n부터 끝까지 범위의 값을 출력하여 최종적으로 오타를 지운 문자열을 출력한다.
