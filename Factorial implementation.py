''' Factorial example implemented with simple iteration '''

def factorial_iterative(n) :
  result = 1

  for i in range(1, n+1) :
    result *= i
  return result

print(factorial_iterative(5)) # result => 120


''' Factorial example implemented using recursive function '''

def factorial_recursive(n) :
  if n <= 1 :
    return 1

  return n * factorial_recursive(n - 1)

print(factorial_recursive(5)) # result => 120
