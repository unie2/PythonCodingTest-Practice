tc = int(input())
count0 = 0
count1 = 0

for _ in range(tc) :
  n = int(input())
  if n == 1 :
    count1 += 1
  else :
    count0 += 1

if count0 > count1 :
  print("Junhee is not cute!")
else :
  print("Junhee is cute!")
