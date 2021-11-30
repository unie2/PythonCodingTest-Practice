a, b = input().split()

value_i = 0
value_j = 0
flag = 0
for i in range(len(a)) :
  for j in range(len(b)) :
    if a[i] == b[j] :
      value_i = i
      value_j = j
      flag = 1
      break
  if flag == 1 :
    break

for i in range(len(b)) :
  for j in range(len(a)) :
    if j == value_i :
      print(b[i], end='')
    else :
      if i == value_j :
        print(a[j], end='')
      else :
        print('.', end='')
  
  print()
  
  
# 1. 이중 for문을 통해 A와 B에 동시에 포함되어 있는 글자이면서, A에서 제일 먼저 등장하는 글자의 인덱스 번호를 구한다.
# 2. 마찬가지로 B에서도 제일 처음 등장하는 글자의 인덱스 번호를 구한다.
# 3. 첫번째 이중 for문이 끝나면 두번째 이중 for문을 통해 문제 설명에 나온 것과 같이 두 단어가 교차된 형태로 출력한다.
