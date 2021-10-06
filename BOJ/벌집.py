n = int(input())

check = 1
room_count = 6
count = 1

while n > check :
  count += 1
  check += room_count
  room_count += 6

print(count)
