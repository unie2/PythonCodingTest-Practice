t = int(input())

for tc in range(1, t + 1) :
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  a.sort()
  b.sort(reverse=True)

  result = 0
  for i in range(len(a)) :
    result += a[i] * b[i]

  print('Case #%d: %d' % (tc, result))
  
  
# 1. 각 테스트케이스마다 a와 b를 입력받아 리스트 형태로 구성한다.
# 2. 스칼라 곱이 가능한 가장 작도록 해야하므로 a는 오름차순으로 정렬하고, b는 내림차순으로 정렬한다.
# 3. 반복문을 통해 리스트 a와 b에 존재하는 값을 하나씩 확인하여 동일한 인덱스의 값을 서로 곱하고 result에 누적한다.
# 4. 반복문이 종료되면 출력 형식에 맞추어 result 값을 출력한다.
