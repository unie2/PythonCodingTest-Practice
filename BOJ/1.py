while True :
  try :
    n = int(input())
    value = '1'
    while True :
      if int(value) % n == 0 :
        print(len(value))
        break
      value += '1'
  except EOFError :
    break
    
    
'''
1. 여러 개의 테스트 케이스로 이루어지므로 try ~ except 를 통해 코드를 작성한다.

2. 처음 value 값은 '1'로 초기화 해준 뒤, 문자 1을 하나씩 추가해주면서 그 값이 배수가 되는지 판별한다.

3. value를 정수형으로 변환한 값을 n으로 나누었을 때 나머지 값이 0이라면 배수이므로, value의 길이를 출력하고 내부 반복작업을 종료한다.

'''
