n = int(input())
data = list(map(int, input().split()))
data.sort()

left = 0
right = len(data) - 1
 
min_value = 1e9
while left < right :
  temp = data[left] + data[right]
  min_value = min(min_value, temp)
  left += 1
  right -= 1

print(min_value)

# 1. 공정성을 위해 data 리스트를 오름차순으로 정렬한다.
# 2. 가장 먼저 제일 왼쪽 값과 오른쪽 값을 더하기 위해 left는 0으로, right는 가장 마지막 인덱스로 초기화한다.
# 3. 반복문을 통해 left인덱스 값과 right인덱스 값을 더하여 temp에 저장한 뒤, min_value와 비교하여 더 작은 값을 min_value에 갱신한다.
# 4. 그 후 left는 1 증가시키고, right는 1 감소시킨다.
# 5. left의 값이 right 값보다 커지게 되면 반복문을 종료한 뒤 최종적으로 min_value 값을 출력한다.
