n = int(input())

a_value = 100
b_value = 100
for _ in range(n) :
  a, b = map(int, input().split())
  if a < b :
    a_value -= b
  elif a > b :
    b_value -= a

print(a_value)
print(b_value)
