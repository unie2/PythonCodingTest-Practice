data = list(map(int, input().split()))

result = 0

for i in range(len(data)) :
  result += (data[i]**2)

print(result%10)
