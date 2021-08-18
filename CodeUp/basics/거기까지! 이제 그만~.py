x = int(input())
result = 0

for i in range(1, x+1) :
  result += i
  if result >= x :
    print(result)
    break
