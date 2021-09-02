''' Case 1 '''
n, m, k = map(int, input().split())
x = list(map(int, input().split()))
result = 0

x.sort()
while True :
  for i in range(k) :
    if m == 0 :
      break
    result += x[n-1]
    m -= 1
  if m == 0 :
    break
  result += x[n-2]
  m -= 1

print(result)


''' Case 2 '''
n, m, k = map(int, input().split())
x = list(map(int, input().split()))

x.sort()
first = x[n - 1]
second = x[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)
