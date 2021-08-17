a, b = input().split()
a2 = bool(int(a))
b2 = bool(int(b))

print((a2 and b2) or ((not a2) and (not b2)))
