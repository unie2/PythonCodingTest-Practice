n = int(input())
data = []
for _ in range(n) :
  data.append(int(input()))

data.sort(reverse=True)

result = 0
for i in range(n) :
  value = data[i] - ((i+1)-1)
  if value > 0 :
    result += value

print(result)


# 1. 입력받은 n개의 자연수를 입력받아 data 리스트에 추가한다.
# 2. 강호가 받을 수 있는 팁의 최댓값을 구해야하므로 내림차순으로 손님의 순서를 정렬한다.
# 3. 반복문을 수행하며, 문제에서 요구한 바와 같이 '원래 주려고 생각했던 돈 - (받은 등수 - 1)' 을 연산하여 value에 할당한다.
# 4. value 값이 음수인 경우 강호는 팁을 받을 수 없으므로, 양수일 경우에만 result에 누적한다.
# 5. 반복문이 종료되면 최종적으로 result 값을 출력한다.
