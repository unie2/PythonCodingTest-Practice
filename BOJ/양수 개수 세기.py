data = list(map(int, input().split()))
result = 0

for i in range(len(data)) :
  if data[i] > 0 :
    result += 1

print(result)


# 1. 정수들을 입력받아 리스트 형태로 구성한다.
# 2. 반복문을 통해 data 리스트에 담겨있는 값들을 하나씩 확인하여 그 수가 0보다 클 경우 즉, 양수일 경우 result를 1 증가시킨다.
# 3. 최종적으로 result 값을 출력한다.
