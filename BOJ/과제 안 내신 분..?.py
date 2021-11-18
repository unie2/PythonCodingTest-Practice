data = [0] * 31

for i in range(28) :
  n = int(input())
  data[n] = 1

for i in range(1, 31) :
  if data[i] == 0 :
    print(i)
    
    
# 1. data 리스트를 구성하여 모두 0으로 값을 초기화한다.
# 2. 반복문을 통해 28개의 출석번호를 입력받아 data리스트의 해당 출석번호 인덱스 값을 1로 갱신한다.
# 3. 반복문을 통해 data 리스트 내에 존재하는 값들을 하나씩 확인하여 해당 값이 0일 경우 인덱스를 출력한다.
