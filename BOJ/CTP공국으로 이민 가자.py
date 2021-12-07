t = int(input())

for _ in range(t) :
  m, case = input().split()
  data = list(input().split())
  if case == 'C' :
    for i in range(len(data)) :
      data[i] = ord(data[i]) - 64
  else :
    for i in range(len(data)) :
      data[i] = chr(int(data[i]) + 64)

  for i in range(len(data)) :
    print(data[i], end=' ')
  
  print()
  
  
# 1. 알파벳 또는 숫자를 입력받아 리스트 형태로 구성한다.
# 2. 입력받은 알파벳(case)가 'C'일 경우 입력받은 data리스트의 각 알파벳을 숫자로 변환하여 갱신한다.
# 3. 입력받은 알파벳(case)가 'N'일 경우 입력받은 data리스트의 각 숫자를 문자로 변환하여 갱신한다.
# 4. 최종적으로 data 리스트에 존재하는 값들을 하나씩 출력 형식에 맞추어 출력한다.
