t = int(input())

for _ in range(t) :
  n = input()
  rev = n[::-1]
  sum_value = str(int(n) + int(rev))
  if sum_value == sum_value[::-1] :
    print("YES")
  else :
    print("NO")
    
    
# 1. rev에 입력받은 n을 뒤집은 값을 할당한다.
# 2. sum_value에 입력받은 n과 뒤집은 rev를 정수형으로 더하여 다시 문자열로 변환한 뒤 저장한다.
# 3. 조건문을 통해 sum_value와 sum_value를 뒤집은 값을 확인하여 일치하면 "YES"를, 일치하지 않다면 "NO"로 출력한다.
