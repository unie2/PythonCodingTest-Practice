n = int(input())
data = input()

score = 0
bonus = 0
for i in range(len(data)) :
  if data[i] == 'O' :
    score += i + 1
    score += bonus
    bonus += 1
  else :
    bonus = 0

print(score)


# 1. 입력받은 문자를 하나씩 확인하여 해당 문자가 'O'일 경우 score에 i + 1 을 누적한다. (인덱스 번호는 0부터 시작하기 때문)
# 2. 또한, score에 보너스 점수도 누적한 후 보너스 점수를 1 증가시킨다.
# 3. 만약 해당 문자가 'X'일 경우 보너스 점수를 0으로 초기화한다.
