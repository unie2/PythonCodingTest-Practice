s = input()

change_0 = 0
change_1 = 0

if s[0] == '0' :
  change_1 += 1
else :
  change_0 += 1

for i in range(len(s) - 1) :
  if s[i] != s[i+1] :
    if s[i+1] == '0' :
      change_1 += 1
    else :
      change_0 += 1

print(min(change_0, change_1))


# 1. 입력받은 문자열 s의 첫 번째 원소에 대하여 그 값이 0이라면 change_1을 1 증가시키고 그렇지 않다면 change_0을 1 증가시킨다.
# 2. 반복문을 통해 두 번째 원소부터 모든 원소를 확인하는데, 현재의 값과 그 다음 값이 다를 경우 다시 조건문을 통해
#   다음 수가 1일 경우 0으로 바꿔준다 생각하여 change_0을 1 증가시킨다. 반대로 다음 수가 0일 경우 1로 바꿔준다고
#   생각하여 change_1을 1 증가시킨다. 이와 같은 작업을 반복하고 최종적으로 change_0과 change_1 중 더 작은 값을 출력한다.
