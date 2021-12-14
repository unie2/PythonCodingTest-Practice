t = int(input())

for _ in range(t) :
  n, m = input().split()
  count_1 = 0
  count_0 = 0

  for i in range(len(m)) :
    if n[i] != m[i] :
      if m[i] == '1' :
        count_1 += 1
      else :
        count_0 += 1

  print(max(count_1, count_0))
  
  
# 1. 이진수 n과 m을 입력받고 반복문을 통해 문자열 n과 m의 문자를 하나씩 확인한다.
# 2. 현재 확인하고 있는 n의 문자와 m의 문자가 다를 경우 m을 기준으로 잡고 다시 조건문을 수행한다.
# 3. 현재 확인하고 있는 m의 문자가 1일 경우 count_1을 1 증가시키고 0일 경우 count_0을 1 증가시킨다.
# 4. 반복문이 종료되면 최종적으로 count_1과 count_0 중에 최댓값을 구해 비트 우정지수를 출력한다.
