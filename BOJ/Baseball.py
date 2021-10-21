t = int(input())

for _ in range(t) :
  y_value = 0
  k_value = 0
  for _ in range(9) :
    y, k = map(int, input().split())
    y_value += y
    k_value += k

  if y_value > k_value :
    print("Yonsei")
  elif y_value < k_value :
    print("Korea")
  else :
    print("Draw")
