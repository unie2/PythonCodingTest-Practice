tc = int(input())

for _ in range(tc) :
  data = list(map(str, input().split()))
  result = float(data[0])
  for i in range(1, len(data)) :
    if data[i] == '@' :
      if data[0] == 0 :
        result += 1
      result *= 3
    elif data[i] == '%' :
      result += 5
    else :
      result -= 7

  print(format(result, ".2f"))
