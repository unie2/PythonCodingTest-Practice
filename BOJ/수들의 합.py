s = int(input())
result = 0
n = 1

while True :
  result += n
  if result > s :
    n -= 1
    break
  n += 1

print(n)
