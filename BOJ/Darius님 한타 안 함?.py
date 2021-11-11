k, d, a = map(int, input().split('/'))

if k + a < d or d == 0 :
  print('hasu')
else :
  print('gosu')
  
  
# 1. '/'로 구분하여 k, d, a에 값을 입력받는다.
# 2. 조건문을 통해 k + a의 값이 d보다 작거나 d의 값이 0일 경우 'hasu'를 출력한다.
# 3. 그렇지 않을 경우 'gosu'를 출력한다.
