def factorial(x) :
  value = 1
  for i in range(2, x + 1) :
    value *= i
  return value

n = int(input())
result = str(factorial(n))

count = 0
for i in range(len(result)-1, -1, -1) :
  if result[i] == '0' :
    count+= 1
  else :
    break

print(count)
