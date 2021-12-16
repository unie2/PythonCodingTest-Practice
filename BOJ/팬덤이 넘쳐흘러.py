n = int(input())
fans = []
for _ in range(n) :
  fans.append(list(map(int ,input().split())))

a = sorted(fans, key=lambda x: x[0])
b = sorted(fans, key=lambda x: x[1])

result = a[-1][0] - b[0][1]

if result <= 0 :
  print(0)
else :
  print(result)
  
  
# 1. n명의 열렬한 팬이 각 학교에 머무르는 시간을 입력받아 fans리스트에 추가한다.
# 2. fans 리스트에서 첫번째 요소를 대상으로 정렬하여 a에 할당한다.
# 3. fans 리스트에서 두번째 요소를 대상으로 정렬하여 b에 할당한다.
# 4. 가장 늦게 등교한 학생에서 가장 빨리 하교한 학생을 뺀 값을 result에 할당한다.
# 5. 조건문을 통해 result의 값이 0보다 작거나 같을 경우 0을 출력하고, 0보다 클 경우 result를 그대로 출력한다.
