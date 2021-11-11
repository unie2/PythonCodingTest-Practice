t = int(input())

for _ in range(t) :
  count = 0
  n, m = map(str, input().split())
  for i in range(int(n), int(m) + 1) :
    for j in range(len(str(i))) :
      if str(i)[j] == '0' :
        count += 1
  print(count)
  
  
# 1. n과 m을 문자열 형식으로 입력받는다.
# 2. 첫번재 반복문을 통해 n부터 m까지의 수들을 하나씩 확인한다.
# 3. 두번째 반복문을 통해 현재 확인하고 있는 값의 각 인덱스 값을 확인한다.
# 4. 조건문을 통해 현재 확인하고 있는 값의 해당 인덱스가 0일 경우 count 값을 1 증가시킨다.
# 5. 반복문이 모두 수행되어 종료되면 count 값을 출력한다.
