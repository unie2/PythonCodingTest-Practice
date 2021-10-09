n = int(input())
data = list(map(int, input().split()))

max_value = max(data)
min_value = min(data)

print(max_value * min_value)
