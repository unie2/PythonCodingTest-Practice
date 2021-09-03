n = int(input())
x = list(map(int, input().split()))
result = 0
count = 0

x.sort()

for i in x :
  count += 1
  if count >= i :
    result += 1
    count = 0

print(result)
