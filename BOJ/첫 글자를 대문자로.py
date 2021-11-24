n = int(input())

for _ in range(n) :
  data = str(input())
  data = data[0].upper() + data[1:]
  print(data)
  
  
# 1. 문자열을 입력받아 첫글자를 대문자로 변환하고 그 이후의 글자들을 붙여 data에 갱신한다.
# 2. 최종적으로 data 값을 출력한다.
