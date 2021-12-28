n = int(input())
score = []

result = 0

for _ in range(n) :
  score.append(int(input()))

for i in range(n-1, 0, -1) :
  
  if score[i] <= score[i - 1] :
    result += (score[i-1] - score[i] + 1)
    score[i-1] = score[i] - 1

print(result)

# 1. n개의 점수를 입력받아 score 리스트에 추가한다.
# 2. 반복문을 통해 score 리스트의 요소들을 거꾸로 하나씩 확인하여 현재 확인하고 있는 값이 앞에 위치한 값보다 작거나 같을 경우 앞에 위치한 값에서 현재 확인하고 있는 값을 빼고, 하나 더 작아야하므로 1을 더하여 result에 누적한다.
# 3. 또한, 앞에 위치한 값을 현재 위치한 값에서 1을 뺀 값으로 갱신한다.
# 4. 반복문이 종료되면 최종적으로 result 값을 출력한다.
