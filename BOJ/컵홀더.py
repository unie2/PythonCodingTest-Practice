n = int(input())
data = input()
result = 0

number = 0
flag = 0
while n > number :
  result += 1
  if data[number] == 'L' :
    number += 2
    flag = 1
  else :
    number += 1

if flag == 1 :
  result += 1

print(result)


# 1. 반복문을 통해 입력받은 문자열의 문자를 하나씩 확인한다.
# 2. 하나의 문자를 확인할 때마다 result를 1 증가시킨다.
# 3. 조건문을 통해 현재 확인하고 있는 문자가 'L' 일 경우 커플석을 의미하고, 한 커플은 컵홀더를 하나 더 사용할 수 있으므로  flag 값을 1로 갱신하고 'LL'은 한 쌍이기 때문에 number 값을 2 증가시킨다.
# 4. 'L'이 아닐 경우 단순히 number 값을 1 증가시켜 다음 문자를 확인하도록 한다.
# 5. 반복문이 종료되면 flag 값을 확인하여 그 값이 1일 경우 커플석이 최소 하나라도 존재하기 때문에 result를 1 증가시킨다.
