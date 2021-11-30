for i in range(2992, 10000) :
  data = i
  sixteen = 0
  while data != 0 :
    sixteen += data % 16
    data //= 16

  data = i
  twelve = 0
  while data != 0 :
    twelve += data % 12
    data //= 12

  data = i
  ten = 0
  while data != 0 :
    ten += data % 10
    data //= 10

  if sixteen == twelve == ten :
    print(i)
    
    
# 1. 싱기한 네자리 숫자의 첫 번째 수는 2992이기 때문에 반복문의 시작 값은 2992로 설정한다.
# 2. data에 i를 담고 sixteen을 초기화하여 while문을 통해 data가 0이 될 때까지 16으로 나눈 나머지 값을 sixteen에 누적한다.
# 3. data에 i를 담고 twelve를 초기화하여 while문을 통해 data가 0이 될 때까지 16으로 나눈 나머지 값을 twelve에 누적한다.
# 4. data에 i를 담고 ten을 초기화하여 while문을 통해 data가 0이 될 때까지 10으로 나눈 나머지 값을 ten에 누적한다.
# 5. 최종적으로 조건문을 통해 sixteen, twelve, ten의 값이 모두 일치할 경우 i를 출력한다.
