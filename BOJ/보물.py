n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0

for i in range(n) :
  result += min(a) * max(b)
  a.pop(a.index(min(a)))
  b.pop(b.index(max(b)))

print(result)
