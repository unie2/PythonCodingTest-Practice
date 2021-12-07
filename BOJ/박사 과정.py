n = int(input())

for _ in range(n) :
  data = input()
  if data == 'P=NP' :
    print('skipped')
  else :
    a, b = map(int, data.split('+'))
    print(a + b)
    
    
# 1. 입력받은 값이 'P=NP'일 경우 'skipped'를 출력한다.
# 2. 그렇지 않은 경우 '+' 연산자를 기준으로 구분하여 a와 b에 정수형으로 해당 값들을 각각 담아 두 수의 합을 출력한다.
