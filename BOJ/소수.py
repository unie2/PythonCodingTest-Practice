m = int(input())
n = int(input())

result = 0
min = 0

for i in range(m, n + 1) :
  flag = 0
  if i == 1 :
    continue
  for j in range(2, i) :
    if i % j == 0 :
      flag = 1
      break
    
  if flag == 0 :
    if min == 0 :
      min = i

    result += i

if result != 0 :
  print(result)
  print(min)
else :
  print(-1)
