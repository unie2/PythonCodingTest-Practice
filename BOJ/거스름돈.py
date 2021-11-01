import sys

n = int(sys.stdin.readline())
value = n % 5

if n == 1 or n == 3 :
  print(-1)
elif value % 2 == 0 :
  print(n // 5 + value // 2)
else :
  print((n // 5) - 1 + (value + 5) // 2)
