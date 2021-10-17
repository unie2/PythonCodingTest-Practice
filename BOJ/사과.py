value = 0
n = int(input())

for _ in range(n) :
  student, apple = map(int, input().split())
  value += apple % student

print(value)
