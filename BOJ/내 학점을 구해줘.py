t = int(input())
for _ in range(t) :
  t2 = int(input())
  c_value = 0
  g_value = 0
  for i in range(t2) :
    c, g = map(str, input().split())
    c_value += int(c)
    g_value += float(c) * float(g)

  result = round(g_value / c_value, 1)
  print(c_value, result)
