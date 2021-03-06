n = int(input())

count = n - 1
for i in range(1, n + 1) :
  print(' ' * count, end='')
  print('* ' * i)
  count -= 1
  
  
'''
1. 초기 공백의 개수는 n - 1개로 설정하여 count를 정의한다.
2. 반복문의 범위는 출력해야할 '*'을 기준으로 하여 1부터 n + 1 까지로 설정한다.
3. 하나의 반복문 작업이 끝날 때마다 공백을 의미하는 count값을 1씩 감소시키도록 하고, '*' 출력 시 우측에 공백을 포함한다. ('* ')

'''
