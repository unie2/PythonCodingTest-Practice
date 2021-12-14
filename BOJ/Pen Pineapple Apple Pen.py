n = int(input())

data = input()

result = 0
i = 0
while i <= n-4 :
  if data[i] == 'p' :
    if data[i+1] == 'P' and data[i+2] == 'A' and data[i+3] == 'p' :
      result += 1
      i += 4
    else :
      i += 1
  else :
    i += 1

print(result)


# 1. 문자열을 입력받아 반복문을 통해 문자를 하나씩 확인한다. index 범위 초과 오류를 예방하기 위해 n-4번째까지만 확인한다.
# 2. 해당 문자가 'p'일 경우 다시 조건문을 통해 다음 문자열이 'PAp'인지 확인하여 맞다면 result를 1 증가시키고 i를 4 증가시킨다.
# 3. 그렇지 않을 경우 단순히 i를 1만 증가시켜 다음 문자를 확인한다.
# 4. 반복문이 종료되면 최종적으로 result 값을 출력한다.
