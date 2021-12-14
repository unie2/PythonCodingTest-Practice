n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)

for i in range(n) :
  data[i] = data[i] + i + 1

print(max(data) + 1)


# 1. 이장님을 최대한 빨리 초대하기 위해 나무가 다 자르는데 걸리는 일수가 높은 순서대로 나무를 심도록 내림차순으로 정렬한다.
# 2. 묘목 하나를 심는데 걸리는 시간은 1일이기 때문에 반복문을 통해 각 일수에 1일을 더한다.
# 3. data 리스트 내에 존재하는 값들 중 최댓값을 구하여 1일을 더하여 출력한다.
