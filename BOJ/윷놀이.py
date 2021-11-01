for _ in range(3) :
  data = list(map(int, input().split()))
  if data.count(1) == 3 :
    print("A")
  elif data.count(1) == 2 :
    print("B")
  elif data.count(1) == 1 :
    print("C")
  elif data.count(0) == 4 :
    print("D")
  else :
    print("E")
