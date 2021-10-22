n = int(input())

while True :
  data = int(input())
  if data == 0 :
    break
  if data % n == 0 :
    print(str(data) + " is a multiple of " + str(n)+".")
  else :
    print(str(data) + " is NOT a multiple of " + str(n)+".")
