k = int(input())

for _ in range(k) :
  p, m = map(int, input().split())
  data = [0] * (m + 1)
  count = 0

  for _ in range(p) :
    value = int(input())
    if data[value] == 0 :
      data[value] = 1
    else :
      count += 1

  print(count)
  
  
# 1. 입력받은 m + 1개 만큼 data 리스트를 구성하여 값은 0으로 초기화한다.
# 2. 각 참가자가 원하는 자리(value)를 입력받아 data리스트의 value자리가 0일 경우 그 자리에 앉을 수 있으며, 해당 값을 1로 갱신한다.
# 3. 0이 아닐 경우 이미 다른 사람이 앉아 있기 때문에 count를 1 증가시킨다.
# 4. 하나의 테스트케이스 내 반복문이 종료되면 최종적으로 count 값을 출력한다.
