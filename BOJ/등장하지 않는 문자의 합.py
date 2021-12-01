t = int(input())

for _ in range(t) :
  data = [0] * 27
  value = input()
  for i in range(len(value)) :
    data[int(ord(value[i]))-65] += 1

  result = 0
  for i in range(26) :
    if data[i] == 0 :
      result += i + 65

  print(result)
  
  
# 1. 입력받은 문자열의 문자를 하나씩 확인하여 아스키코드 값으로 변환한 뒤 65로 뺀 값을 data 리스트의 인덱스로 하여 해당 인덱스의 값을 1 증가시킨다.
# 2. 첫번째 반복문이 끝나면 data 리스트의 값을 하나씩 확인하여 그 값이 0이면 등장하지 않는 문자이기 때문에 i에 65를 더하여 result에 누적한다. 
# 3. 최종적으로 result를 출력한다.
