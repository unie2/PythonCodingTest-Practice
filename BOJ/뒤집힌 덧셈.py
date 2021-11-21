def rev_function(x) :
  value = ""
  for i in range(len(x)-1, -1, -1) :
    value += x[i]
  return int(value)

x, y = map(str, input().split())

sum_value = rev_function(x) + rev_function(y)

print(rev_function(str(sum_value)))


# 1. 각 x와 y를 문자열로 입력받는다.
# 2. rev_function( ) 함수를 통해 전달받은 문자열의 값을 거꾸로 하나씩 확인하여 value에 문자를 추가한다.
# 3. 구성된 value값을 정수형으로 변환하여 반환한다.
# 4. 반환된 x값과 y값을 더하여 sum_value에 할당한다.
# 5. sum_value를 문자열로 변환한 뒤 다시 rev_function( ) 함수를 통해 역순으로 바꿔 출력한다.
