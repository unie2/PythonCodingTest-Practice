tc = int(input())

price = [350.34, 230.90, 190.55, 125.30, 180.90]

for _ in range(tc) :
  sum = 0
  data = list(map(float, input().split()))
  for i in range(5) :
    sum += price[i] * data[i]

  print("$%.2f" % sum)
  
  
# price 리스트에 블래스터 라이플, 시각 센서, 청각 센서, 팔, 다리의 각 가격을 할당한다.
# 범위가 5인 반복문을 통해 price 리스트의 i번째 값에 입력받은 data 리스트의 i번째 값을 곱하여 sum에 누적해간다.
# 최종적으로 입력으로 주어진 부품을 모두 구매하는데 핑료한 비용을 소수점 둘째 자리까지 출력한다.
