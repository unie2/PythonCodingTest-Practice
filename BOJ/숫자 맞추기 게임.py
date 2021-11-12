number = 0

while True :
  n = int(input())
  number += 1
  if n == 0 :
    break
  if n % 2 != 0 :
    print(number, ". odd ", n//2, sep='')
  else :
    print(number, ". even ", n//2, sep='')
    
    
# 1. 매 출력 시 케이스 번호와 함께 출력해야 하므로 number를 0으로 초기화한 뒤 반복문 내에서 한 작업을 수행할  때마다 number값을 1씩 증가시킨다.
# 2. 조건문을 통해 입력받은 n이 0일 경우 반복문을 종료한다.
# 3. 0이 아닐 경우 조건문을 통해 입력받은 n이 홀수일 경우 케이스 번호와 함께 출력형식에 맞추어 n을 2로 나눈 몫을 출력한다.
# 4. 입력받은 n이 짝수일 경우 케이스 번호와 함께 출력형식에 맞추어 n을 2로 나눈 몫을 출력한다.
