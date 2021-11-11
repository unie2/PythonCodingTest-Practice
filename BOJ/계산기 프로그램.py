first = int(input())

while True :
  oper = input()
  if oper == '=' :
    break
  n = int(input())
  if oper == '+' :
    first += n
  elif oper == '-' :
    first -= n
  elif oper == '*' :
    first *= n
  else :
    first //= n

print(first)


# 1. 첫번째 입력값은 피연산자 즉, 정수형 숫자이기 대문에 먼저 입력받아 first에 할당한다.
# 2. while문을 통해 입력받은 값이 '='일 때까지 반복 수행한다.
# 3. 반복문 내에서는 연산자와 피연산자를 입력받아 다시 연산자의 값을 확인한다.
# 4. 값이 '+'일 경우 first에 입력받은 n을 더하여 다시 first 값을 갱신한다.
# 5. 값이 '-'일 경우 first에 입력받은 n을 빼고 다시 first 값을 갱신한다.
# 6. 값이 '*'일 경우 first에 입력받은 n을 곱하여 다시 first 값을 갱신한다.
# 7. 값이 '/'일 경우 first에 입력받은 n을 나눈 몫을 구하여 다시 first에 값을 갱신한다.
