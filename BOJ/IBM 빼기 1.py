n = int(input())

for x in range(1, n+1) :
  data = input()
  result = ''
  for i in range(len(data)) :
    value = ord(data[i]) + 1
    if value > 90 :
      value = 65
    result += chr(value)
    
  print('String #%d' % x)
  print(result)
  print()
  
  
# 1. 입력받은 문자열의 길이만큼 반복문을 수행하여 문자를 하나씩 확인한다.
# 2. 현재 확인하고 있는 문자를 아스키코드 값으로 변환하여 1을 더한 값을 value에 할당한다.
# 3. value의 값이 90을 초과할 경우 Z에서 A로 넘어가야하기 때문에 value의 값을 65로 갱신한다.
# 4. value 값을 문자로 변환하여 result에 붙인다.
# 5. 최종적으로 출력형식에 맞추어 result값을 출력한다.
