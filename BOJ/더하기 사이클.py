n = int(input())
temp = n
count = 0

while True :
  one = temp % 10
  two = temp // 10
  get = (one + two) % 10
  temp = (one * 10) + get
  count += 1
  if temp == n :
    break

print(count)
