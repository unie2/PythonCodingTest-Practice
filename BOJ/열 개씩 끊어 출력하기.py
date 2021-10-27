value = input()
count = 0

for i in range(len(value)) :
  print(value[i], end='')
  count += 1
  if count == 10 :
    print()
    count = 0
