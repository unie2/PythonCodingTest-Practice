data = list(input())

start = 'A'
result = 0

for i in data :
  left_value = ord(start) - ord(i)
  right_value = ord(i) - ord(start)

  if left_value < 0 :
    left_value += 26
  elif right_value < 0 :
    right_value += 26

  result += min(left_value, right_value)
  start = i

print(result)


# 1. 알파벳 대문자로 구성된 문자열을 입력받아 리스트 형태로 구성하고 data에 저장한다.
# 2. 처음 순간의 화살표는 'A'를 가리키므로 start에 문자 'A'를 할당한다.
# 3. data 리스트에 존재하는 문자들을 하나씩 확인하여 start의 아스키코드 값에서 현재 확인하고 있는 문자의 아스키코드 값을 빼 left_value에 할당한다.
# 4. 현재 확인하고 있는 문자의 아스키코드 값에서 start의 아스키코드 값을 빼 right_value에 할당한다.
# 5. left_value의 값이 음수일 경우 26을 더하고, right_value의 값이 음수일 경우 26을 더한다.
# 6. 두 수(left_value, right_value)의 값을 비교하여 더 작은 값을 result에 누적한 후 start를 현재 확인한 값으로 갱신한다.
