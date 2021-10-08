burger_data = []
drink_data = []

for _ in range(3) :
  burger_data.append(int(input()))

for _ in range(2) :
  drink_data.append(int(input()))
  
burger_data.sort()
drink_data.sort()

print(burger_data[0] + drink_data[0] - 50)
