n = int(input())
data = list(map(int, input().split()))

number = 0
result = 0
for i in range(len(data)) :
  if data[i] == number :
    result += 1
    number += 1
  
  if number > 2 :
    number = 0

print(result)


# 1. 반복문을 통해 data 리스트 값을 하나씩 확인한다.
# 2. 현재 확인하고 있는 값이 number와 일치할 경우 result에 1을 증가시키고, number 값을 1 증가시킨다.
# 3. number는 0, 1, 2, 0, 1, 2 ... 순으로 반복되어야 하기 때문에 number의 값이 2보다 클 경우 0으로 갱신한다.
# 4. 반복문 종료 후 최종적으로 result 값을 출력한다.
