tc = int(input())

for _ in range(tc) :
  a, b = map(int, input().split())
  
  a_value, b_value = a, b
  while b_value != 0 :
    a_value = a_value % b_value
    a_value, b_value = b_value, a_value

  print(a*b // a_value)
