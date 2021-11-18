while True :
  lower = 0
  upper = 0
  number = 0
  blank = 0

  try :
    s = input()
    for i in range(len(s)) :
      if 97 <= ord(s[i]) <= 122 :
        lower += 1
      elif 65 <= ord(s[i]) <= 90 :
        upper += 1
      elif s[i] == ' ' :
        blank += 1
      else :
        number += 1
  except :
    break
  
  print(lower, upper, number, blank)
  
  
# 1. 입력 횟수에 제한이 없기 때문에 try ~ except 문을 활용하여 계속해서 입력받을 수 있도록 한다.
# 2. 반복문을 통해 입력받은 문자열의 문자를 하나씩 확인하여 그 값을 아스키코드 값으로 변환한다.
# 3. 해당 아스키코드 값이 97 이상 122 이하라면 소문자에 해당하기 때문에 lower에 1을 증가시킨다.
# 4. 해당 아스키코드 값이 65 이상 90 이하라면 대문자에 해당하기 때문에 upper에 1을 증가시킨다.
# 5. 해당 문자가 공백일 경우 blank에 1을 증가시킨다.
# 6. 모두 그렇지 않을 경우 number에 1을 증가시킨다.
# 7. 최종적으로 각각의 문자열에 대해서 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력한다.
