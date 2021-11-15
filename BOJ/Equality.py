data, result = map(str, input().split(' = '))

if int(eval(data)) == int(result) :
  print('YES')
else :
  print('NO')
  
  
# 1. 입력받은 문자열을 '='로 구분하여 각 data와 result에 할당한다.
# 2. 조건문에서 eval( )을 사용하여 data의 식의 결과가 result와 같을 경우 'YES'를 출력한다.
# 3. 그렇지 않을 경우 'NO'를 출력한다.
