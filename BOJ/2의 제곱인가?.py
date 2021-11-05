n = int(input())

data = [2**i for i in range(31)]

if n in data :
  print(1)
else :
  print(0)
  
  
# 30까지로 범위를 지정하여 2의 제곱수들을 data 리스트에 저장한다.
# 조건문을 통해 입력받은 n이 data 리스트 내에 존재할 경우 2의 제곱수이기 때문에 1을 출력하고 그렇지 않을경우 0을 출력한다.
