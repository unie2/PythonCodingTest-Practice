t = int(input())

for _ in range(t) :
  n, m = map(int, input().split())
  u = (m*2) - n
  t = n - m
  print(u, t)

  
  
# 각 테스트 케이스마다 모든 닭의 다리수의 합(n)과 닭의 수(m)을 입력받고
# 닭 한마리당 다리의 수는 2개이기 때문에 m*2 - n 을 계산하여 다리가 잘린 닭의 수(u)를 구하고
# n - m을 계산하여 멀쩡한 닭의 수(t)를 구하여 출력한다.
