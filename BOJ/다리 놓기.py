tc = int(input())

def factorial(x) :
  count = 1
  for i in range(2, x + 1) :
    count *= i
  
  return count

for _ in range(tc) :
  a, b = map(int, input().split())
  result = factorial(b) // (factorial(a) * factorial(b-a))
  print(result)
