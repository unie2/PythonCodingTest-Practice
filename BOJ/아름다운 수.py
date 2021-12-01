t = int(input())

for _ in range(t) :
  x = input()
  data = []

  result = 0
  for i in range(len(x)) :
    if int(x[i]) not in data :
      result += 1
      data.append(int(x[i]))

  print(result)
  
  
# 1. 아름다운 정도를 알고 싶은 수(x)를 문자열 형태로 입력받아 문자를 하나씩 정수형으로 변환하여 확인한다.
# 2. 해당 정수가 data 리스트에 존재하지 않을 경우 result값을 1 증가시키고 data 리스트에 해당 값을 추가한다.
# 3. 반복문이 모두 끝나면 최종적으로 result 값을 출력한다.
