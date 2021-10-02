a, b, c = int(input()), int(input()), int(input())
data = a * b * c
arr = [0] * 10

while True :
  arr[data % 10] += 1
  data //= 10
  if data == 0 :
    break

for i in range(10) :
  print(arr[i])
