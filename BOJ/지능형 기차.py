data = []
count = 0

for _ in range(4) :
  down, up = map(int, input().split())
  count -= down
  count += up

  data.append(count)

print(max(data))
