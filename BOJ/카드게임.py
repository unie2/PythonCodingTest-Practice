a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_count = 0
b_count = 0
for i in range(10) :
  if a[i] == b[i] :
    continue
  elif a[i] > b[i] :
    a_count += 1
  else :
    b_count += 1

if a_count == b_count :
  print('D')
elif a_count > b_count :
  print('A')
else :
  print('B')
  
  
# 1. A의 카드와 B의 카드의 각 라운드별 카드 값을 리스트 형태로 구성하여 입력받는다.
# 2. 반복문을 통해 각 라운드별 수를 비교하여 A의 i번째 라운드 값이 B의 값보다 더 크면 a_count를 1 증가시킨다.
# 3. B의 i번째 라운드 값이 A의 값보다 더 크면 b_count를 1 증가시킨다.
# 4. 반복문 수행이 끝나면 조건문을 통해 a_count와 b_count를 비교하고, 두 수가 같을 경우 비겼기 때문에 'D'를 출력한다.
# 5. a_count의 값이 더 클 경우 'A'를 출력하고, b_count의 값이 더 클 경우 'B'를 출력한다.
