n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
m = price[0]

for i in range(n - 1) :
  if price[i] < m :
    m = price[i]
  result += distance[i] * m

print(result)


# 1. 첫번째 주유소는 무조건 가야하므로 m에 첫번째 주유소의 리터당 가격을 할당한다.
# 2. n - 1까지의 범위로 반복문을 수행하는데, 현재 확인하고 있는 가격과 m을 비교한 후, m이 더 크다면 현재 확인하고 있는 가격으로 갱신한다.
# 3. m에 현재까지의 최소 비용이 담겨져 있으므로, 현재 확인하고 있는 거리 값에 m을 곱하여 result에 누적한다.
# 4. 반복문이 종료되면 최종적으로 result를 출력한다.
