while True :
  value = input()
  if value == '#' :
    break
  result = 0
  number = -1
  for i in range(len(value)-1, -1, -1) :
    if value[i] == '-' :
      number += 1
    elif value[i] == '\\' :
      number += 1
      result += 8 ** number
    elif value[i] == '(' :
      number += 1
      result += 2 * (8 ** number)
    elif value[i] == '@' :
      number += 1
      result += 3 * (8 ** number)
    elif value[i] == '?' :
      number += 1
      result += 4 * (8 ** number)
    elif value[i] == '>' :
      number += 1
      result += 5 * (8 ** number)
    elif value[i] == '&' :
      number += 1
      result += 6 * (8 ** number)
    elif value[i] == '%' :
      number += 1
      result += 7 * (8 ** number)
    else :
      number += 1
      result += -1 * (8 ** number)

  print(result)
  
  
# 1. 입력받은 문자가 '#'일 때까지 while문을 통해 반복 수행한다.
# 2. 반복문을 통해 입력받은 문자열을 거꾸로 하나씩 확인하여 해당되는 문자에 대하여 number값을 1 증가시키고
#    문제에서 제시한 각 기호에 대응하는 숫자에 8진법 계산형식을 적용하여 result에 누적한다.
# 3. 문자열에 존재하는 모든 문자를 하나씩 모두 확인하여 수행한 뒤 최종적으로 result를 출력한다.
