a, b = map(str, input().split())

a = int(a, 2)
b = int(b, 2)

sum_value = a + b

print(bin(sum_value)[2:])
