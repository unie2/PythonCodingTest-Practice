''' Case 1 '''
n, m = map(int, input().split())
result = 0

for i in range(n) :
  x = list(map(int, input().split()))
  search = 10001
  for j in x :
    search = min(search, j)
  result = max(result, search)

print(result)
