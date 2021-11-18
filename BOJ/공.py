m = int(input())

data = [1, 0, 0]
for _ in range(m) :
  x, y = map(int, input().split())
  data[x-1], data[y-1] = data[y-1], data[x-1]

for i in range(3) :
  if data[i] == 1 :
    print(i + 1)
    
    
# 1. 문제에서 컵 개수가 3개로 제한되어 있기 때문에 data 리스트를 구성하여 첫번째 인덱스에 공이 있음을 의미하는 1을 할당하고 나머지 인덱스 값은 0으로 할당한다.
# 2. 반복문을 통해 x와 y를 입력받아 컵의 위치를 서로 바꿔주도록 한다.
# 3. 반복문을 통해 data 리스트의 값을 하나씩 확인하여 해당 인덱스 값이 1이라면 인덱스 값 + 1 을 출력한다.
