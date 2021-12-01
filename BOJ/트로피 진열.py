n = int(input())
data = []

for _ in range(n) :
  data.append(int(input()))

left_max_value = 0
left_result = 0
for i in range(len(data)) :
  if data[i] > left_max_value :
    left_max_value = data[i]
    left_result += 1

right_max_value = 0
right_result = 0
for i in range(len(data)-1, -1, -1) :
  if data[i] > right_max_value :
    right_max_value = data[i]
    right_result += 1

print(left_result)
print(right_result)


# 1. n개의 값을 입력받아 리스트 형태로 구성한다.
# 2. 왼쪽에서 봤을 때의 경우에는 반복문의 범위를 0부터 data 리스트의 길이까지로 설정한다.
# 3. 조건문을 통해 현재 확인하고 있는 data리스트의 값이 left_max_value보다 클 경우 left_max_value를 data[i]의 값으로 갱신하고 left_result의 값을 1 증가시킨다.
# 4. 오른쪽에서 봤을 때의 경우에는 반복문의 범위를 거꾸로 설정한다.
# 5. 조건문을 통해 현재 확인하고 있는 data리스트의 값이 right_max_value보다 클 경우 right_max_value를 data[i]의 값으로 갱신하고 right_result의 값을 1 증가시킨다.
# 6. 최종적으로 left_result와 right_result 값을 출력 형식에 맞추어 출력한다.
