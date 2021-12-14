case_number = 1

while True :
  l, p, v = map(int, input().split())
  if l == p == v == 0 :
    break
  value = v // p

  result = l * value
  result += min((v%p), l)

  print('Case %d: %d' % (case_number, result))
  case_number += 1
  
  
# 1. 각 테스트케이스를 출력하기 위해 case_number를 1로 초기화하여 선언한다.
# 2. 입력받은 l, p, v 모두 0일 때까지 while문을 통해 반복수행한다.
# 3. 반복문 내부에서는 v//p (강산이가 캠핑장을 온전히 이용할 수 있는 일수) 를 구해 value에 할당한다.
# 4. 구한 value 값과 입력받은 l 값을 곱하여 result에 할당한다.
# 5. 휴가일 v 중 (v%p)와 입력받은 l을 비교하여 더 작은 일수를 result에 누적한다.
# 6. 최종적으로 해당 테스트케이스 값과 함께 result 값을 출력한 후 다음 테스트케이스를 위해 case_number을 1 증가시킨다.
