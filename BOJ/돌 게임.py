n = int(input())
count = 0

while n > 0 :
  count += 1
  if n >= 3 :
    n -= 3
  else :
    n -= 1

if count % 2 == 0 :
  print("CY")
else :
  print("SK")
