a, r, n = map(int, input().split())
result = a
count = 1

while(1) :
  result *= r
  count += 1
  if count == n :
    break

print(result)
