import sys

n = int(input())
result = 0

for _ in range(n) :
  x = int(sys.stdin.readline())
  result += x

print(result - (n - 1))
