s = input()
target = input()
result = 0

num = 0
while num <= len(s) - len(target) :
  if s[num:num+len(target)] == target :
    result += 1
    num += len(target)
  else :
    num += 1

print(result)


# 1. 문자열 s의 길이 - 문자열 target의 길이를 뺀 값이 num보다 작아질 때까지 while문을 통해 반복문을 수행한다.
# 2. 문자열 s의 특정 범위와 입력받은 target값이 같을 경우 result를 1증가시킨 후, num값을 target의 길이로 갱신한다.
# 3. 그렇지 않을 경우 단순히 num 값만 1 증가시킨다.
# 4. 반복문이 종료되면 최종적으로 result 값을 출력한다.
