import math

def isPrime(x) :
  for i in range(2, int(math.sqrt(x) + 1)) :
    if x % i == 0 :
      return False
    
  return True

n = int(input())
min_value = 0

for i in range(n, 1000001) :
  if i == 1 :
    continue
  if str(i) == str(i)[::-1] :
    if isPrime(i) :
      min_value = i
      break

if min_value == 0 :
  min_value = 1003001

print(min_value)
