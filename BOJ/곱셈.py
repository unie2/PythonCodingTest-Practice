a, b = int(input()), int(input())

one = b % 10
two = (b % 100) // 10
three = (b % 1000) // 100

print(a * one)
print(a * two)
print(a * three)
print(a * b)
