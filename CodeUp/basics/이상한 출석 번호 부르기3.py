n = int(input())
x = list(map(int, input().split()))
min = x[0]

for i in range(n) :
  if x[i] < min :
    min = x[i]

print(min)
