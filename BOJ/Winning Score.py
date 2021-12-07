apple = 0
banana = 0

for i in range(3, 0, -1) :
  apple += i * int(input())

for i in range(3, 0, -1) :
  banana += i * int(input())

if apple == banana :
  print('T')
elif apple > banana : 
  print('A')
else :
  print('B')
  
  
# 1. 각 입력받는 3개의 점수는 3점, 2점, 1점 순으로 입력되기 때문에 단순히 반복문을 통해 3부터 1(포함)까지 1씩 감소하면서 범위를 지정하고 수행할 수 있다.
# 2. 조건문을 통해 사과의 점수와 바나나의 점수가 동일하다면 'T'를 출력한다.
# 3. 사과의 점수가 바나나의 점수보다 크다면 'A를 출력하고, 반대일 경우 'B'를 출력한다.
