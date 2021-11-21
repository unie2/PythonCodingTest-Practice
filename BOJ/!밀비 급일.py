while True :
  data = input()
  if data == "END" :
    break
  result = ""
  for i in range(len(data)-1, -1, -1) :
    result += data[i]

  print(result)
  
  
# 1. while문을 통해 입력받은 값이 "END"일 때까지 반복 수행한다.
# 2. while문 내부에서는 result를 문자열 타입으로 선언하고 반복문을 통해 입력받은 문자열을 거꾸로 뒤집어 구성한다.
# 3. 최종적으로 암호가 해독된 것(result)을 출력한다.
