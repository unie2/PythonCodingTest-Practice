tc = int(input())

for _ in range(tc) :
  data, result = map(str, input().split('='))

  if eval(data) == int(result) :
    print('correct')
  else :
    print('wrong answer')
    
    
# 1. '='로 구분하여 입력받은 문자열을 각각 data와 result에 담는다.
# 2. 조건문에서 eval( )를 사용하여 data에 대한 식이 result와 같을 경우 'correct'를 출력한다.
# 3. 그렇지 않을 경우 data 식과 답이 일치하지 않기 때문에 'wrong answer'를 출력한다.
