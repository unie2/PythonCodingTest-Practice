n = int(input())

a_score = 0
b_score = 0

for _ in range(n) :
  a, b = map(int, input().split())
  if a > b :
    a_score += 1
  elif b > a :
    b_score += 1

print(a_score, b_score)


# 1. a의 점수가 b의 점수보다 크면 a_score를 1 증가시킨다.
# 2. b의 점수가 a의 점수보다 크면 b_score를 1 증가시킨다.
# 3. 최종적으로 a_score와 b_score를 출력한다. (부분 성공)
