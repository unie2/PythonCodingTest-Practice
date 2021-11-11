n = int(input())
count = 0

while True :
  if n == 1 :
    count += 1
    break
  if n % 2 == 0 :
    n //= 2
    count += 1
  else :
    n = 3 * n + 1
    count += 1

print(count)


# 1. while문을 통해 n의 값이 1이 될때까지 반복 수행한다.
# 2. while문 내에서는 조건문을 통해 n의 값이 짝수일 경우 n을 2로 나눈 몫을 다시 n에 갱신한다. 
# 해당 작업이 끝나면 count 값을 1 증가시킨다.
# 3. n의 값이 홀수일 경우 3 * n + 1 과 같이 계산하여 다시 n에 갱신한다.
# 해당 작업이 끝나면 count 값을 1 증가시킨다.
# 4. n이 1일 될 경우 해당 수행작업 횟수도 포함시켜야하기 때문에 count값을 1 증가시킨 후 반복문을 종료한다.
