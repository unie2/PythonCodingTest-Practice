t = int(input())

for _ in range(t) :
  n = int(input())
  number = 2

  data = {}
  for i in range(n + 1) :
    data[i] = 0

  while n > 1 :
    if n % number != 0 :
      number += 1
    else :
      n /= number
      data[number] += 1

  for i in data.items() :
    if i[1] != 0 :
      print(i[0], i[1])
      
      
# 반복문을 통해 딕셔너리의 값들을 0으로 초기화하고 n이 1보다 작거나 같아질 때까지 while문을 수행한다.
# while문 내에서는 조건문을 통해 입력받은 n을 정의되어 있는 number값으로 나눈 나머지 값을 확인하여 그 값이
# 1이 아닐 경우 number값을 1 증가시키도록 하고, 나머지 값이 0일 경우 n을 number로 나눈 몫으로 다시 갱신한다.
# 갱신한 후에는 data 딕셔너리의 number 인덱스의 값을 1 증가시키도록 한다.
# while문이 종료되면 data 딕셔너리에 있는 값들을 불러와 0이 아닌 값을 출력한다.
