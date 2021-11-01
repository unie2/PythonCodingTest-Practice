data = []

for _ in range(6) :
  data.append(int(input()))

max_value1 = sorted(data[:4])
max_value2 = data[4:]

print(sum(max_value1[1:]) + max(max_value2))
