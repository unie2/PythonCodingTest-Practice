a, b, c, m = map(int, input().split())

day = 0

result = 0
count = 0

if a > m :
  print(0)
else :
  while day != 24 :
    day += 1
    if count + a <= m :
      result += b
      count += a
    else :
      if count - c >= 0 :
        count -= c
      else :
        count = 0

  print(result)
  
  
# 1. 초기 피로도는 0이며, 피로도(a)가 번아웃 경계(m)보다 클 경우 일을 하나라도 처리할 수 없기 때문에 0을 출력한다.
# 2. 그렇지 않을 경우 반복문을 통해 24시간동안 수행하도록 한다.
# 3. 조건문을 통해 피로도를 의미하는 count에 입력받은 피로도 값 a를 더한 값이 m보다 작거나 같을 경우 일을 처리할 수 있기 때문에 처리한 일의 양(result)에 b를 누적하고, count값에 a를 누적한다.
# 4. 그렇지 않을 경우 한 시간을 쉬어야 하는데, 피로도는 0보다 작아질 수 없으므로, 조건문을 통해 count - c의 값이 0보다 클 경우에 해당 연산을 수행하고, 그렇지 않을 경우에는 피로도(count)를 0으로 갱신한다.
# 5. 24시간이 지나면 반복문이 종료되고, 최종적으로 result 값을 출력한다.
