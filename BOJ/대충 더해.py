a, b = map(str, input().split())
max_len = 0
if len(a) > len(b) :
  max_len = len(a)
  b = '0' * (len(a) - len(b)) + b
elif len(a) < len(b) :
  max_len = len(b)
  a = '0' * (len(b) - len(a)) + a
else :
  max_len = len(b)

result = ''
for i in range(max_len) :
  result += str(int(a[i]) + int(b[i]))

print(result)


# 1. 입력받은 두 수 중 문자열 길이가 더 긴 값을 기준으로 하여 해당 길이를 max_len에 할당하고, 길이가 더 짧은 값 앞에 부족한 자리수만큼 0으로 채워주도록 하여 길이를 서로 맞춰준다.
# 2. 만약 두 수의 문자열 길이가 같을 경우에는 max_len에 할당하는 작업만 수행한다.
# 3. 반복문을 통해 a와 b 각 자리의 문자를 하나씩 확인하여 정수형으로 변환하여 두 수를 더해주고 다시 문자열로 변환하여 result에 추가한다.
