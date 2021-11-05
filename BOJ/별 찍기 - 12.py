n = int(input())
area = n

for i in range(1, n + 1) :
  print(' '*(area-i) + '*'*i)

for i in range(1, area) :
  print(' '*(i) + '*'*(area-i))
  
  
# 입력받은 수를 바탕으로 반복문을 통해 문제에서 요구하는 출력형식에 맞추어 별을 출력한다.
