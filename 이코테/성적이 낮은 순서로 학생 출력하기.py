n = int(input())
arr = []

for i in range(n) :
  data = input().split()
  arr.append((data[0], int(data[1])))

result = sorted(arr, key=lambda score: score[1])

for score in result :
  print(score[0], end= ' ')
