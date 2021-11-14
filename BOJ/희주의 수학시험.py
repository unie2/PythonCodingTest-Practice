data = []

a, b = map(int, input().split())
value = count = 1
for _ in range(b) :
  data.append(value)
  if value == count :
    count = 0
    value += 1
  count += 1

print(sum(data[a-1:b]))


# 1. 리스트에 추가할 값을 의미하는 value와 해당 수만큼 카운트를 세기위한 count를 1로 초기화한다.
# 2. 반복문을 통해 data리스트에 1부터 시작하여 값을 추가한다.
# 3. 조건문을 통해 그 값과 count값이 같을 경우 count를 0으로 다시 갱신하고 value 값을 1 증가시킨다.
# 4. 하나의 반복 작업이 끝날 무렵 count값을 1 증가시킨다.
# 5. 반복 작업이 모두 끝나면 최종적으로 입력받은 a부터 b까지의 범위 인덱스 값의 합을 구하여 출력한다.
