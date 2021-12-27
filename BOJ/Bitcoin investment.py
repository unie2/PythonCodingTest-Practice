n = int(input())
data = list(map(int, input().split()))

max_value = 0
for i in range(len(data) - 1) :
  value = max(data[i::])
  max_value = max(max_value, value - data[i])

print(max_value)


# 1. 반복문을 통해 data 리스트에 존재하는 값을 하나씩 확인하는데, 한번의 수행마다 현재 확인하고 있는 값부터 마지막  인덱스까지 중에 최댓값을 구해 value에 할당한다.
# 2. 현재 저장되어 있는 최댓값(max_value)과 value - data[i]의 값을 비교하여 더 큰 값을 max_value로 갱신한다.
# 3. 반복문이 종료되면 최종적으로 max_value 값을 출력한다.
