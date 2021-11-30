while True :
  data = input()
  if data == '#' :
    break
  value = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  result = 0
  for i in range(len(data)) :
    if data[i] in value :
      result += 1

  print(result)
  
  
# 1. 입력받은 값이 '#'일 때까지 while문을 통해 반복 수행한다.
# 2. value를 리스트 형태로 구성하고 내부 값에는 모음의 소문자, 대문자를 모두 할당한다.
# 3. 입력받은 문자열의 길이만큼 반복문을 수행하여 현재 확인하고 있는 문자가 value에 존재할 경우 result를 1 증가한다.
# 4. 최종적으로 result를 출력한다.
