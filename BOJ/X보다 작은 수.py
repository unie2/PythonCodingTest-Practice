n, x = map(int, input().split())

result = list(map(int, input().split()))

for i in range(n) :
  if result[i] < x :
    print(result[i], end=' ')
