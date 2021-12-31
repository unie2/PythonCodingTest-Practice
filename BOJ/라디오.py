a, b = map(int, input().split())
n = int(input())
data = []
for _ in range(n) :
  data.append(int(input()))

target = 1e9

for i in data :
  if abs(i - b) < abs(target - b) :
    target = i

result = 1
if target > b :
  result += target - b
else :
  result += b - target

if abs(a - b) < result :
  print(abs(a-b))
else :
  print(result)
  
# 1. data 리스트 내 요소를 하나씩 확인하는데, 요소값에서 듣고싶은 주파수를 뺀 절대값이 현재의 target값에서 듣고싶은 주파수를 뺀 절대값보다 작을 경우 target값을 현재 요소값으로 갱신한다.
# 2. 모든 요소를 다 확인하였다면 현재 target값에는 듣고싶은 주파수와의 거리가 가장 짧은 값이 할당되어 있다.
# 3. 미리 지정되어 있는 주파수로 한 번 이동했기 때문에 result를 1로 초기화한다.
# 4. target 값에서 b로 이동해야하므로 두 수의 차이를 result에 누적한다.
# 5. 최종적으로 조건문을 통해 result 값이 더 작은지, 현재 주파수(a)에서 b로 가는 거리가 더 작은지 비교하여 더 작은 거리를 출력한다.
