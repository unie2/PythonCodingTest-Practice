n, w = map(int, input().split())
data = []
for _ in range(n) :
  data.append(int(input()))

coin = 0
for i in range(n-1) :
  if data[i] < data[i+1] :
    if w // data[i] > 0 :
      coin = w // data[i]
      w -= data[i] * coin
  elif data[i] > data[i-1] :
    w += data[i] * coin
    coin = 0

if coin > 0 :
  w += coin * data[-1]

print(w)


# 1. n개의 바이트 코인 가격을 입력받아 data리스트에 추가한다.
# 2. data리스트 내 하나의 값을 확인할 때마다 다음 값을 확인해야하므로 반복문의 범위는 n-1로 지정하여 수행한다.
# 3. 조건문을 통해 현재 확인하고 있는 값이 다음 값보다 작고 상승하려는 그래프라면 w//data[i]개의 코인을 매수한다.
# 4. 만약 현재 확인하고 있는 값이 이전의 값보다 클 경우 매도하여 w에 누적하고, coin값을 0으로 다시 초기화시켜준다.
# 5. 반복문이 종료되면 조건문을 통해 아직 매도하지 않은 값이 있는지 확인하여 있다면 마지막 마지막 코인 가격에 현재의 coin 값을 곱하여 매도해줌으로써 w에 값을 누적한다. 
# 6. 최종적으로 가지고 있는 현금의 최댓값(w)을 출력한다.
