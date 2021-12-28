n = int(input())
data = []

for _ in range(n) :
  data.append(int(input()))

data.sort(reverse=True)
result = 0
count = 1

for i in data :
  if count % 3 != 0 :
    result += i
    count += 1
  else :
    count += 1

print(result)


# 1. 최소비용을 구해야하므로, 최대한 비싼 가격을 무료로 받기 위해 입력받은 값들을 내림차순으로 정렬한다.
# 2. 리스트 내 요소를 하나씩 세기 위해 count를 1로 초기화하고, 반복문 내에서 count값을 3으로 나눈 값을 확인한다.
# 3. 3으로 나눈 값이 0이 아닐 경우 현재 확인하고 있는 요소 값을 result에 누적한 뒤 count를 1 증가시킨다.
# 4. 그렇지 않을 경우 단순히 count를 1 증가시킨다.
# 5. 리스트 요소를 모두 확인한 후 최종적으로 result 값을 출력한다.
