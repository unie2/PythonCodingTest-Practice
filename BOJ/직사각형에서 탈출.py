x, y, w, h = map(int, input().split())
w -= x
h -= y

if x > w :
  x = w
if y > h :
  y = h

if x > y :
  print(y)
else :
  print(x)
