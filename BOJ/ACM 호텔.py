tc = int(input())

for _ in range(tc) :
  h, w, n = map(int, input().split())
  if n % h == 0 :
    print('%d%02d'%(h, n/h))
  else :
    print('%d%02d'%(n%h, n/h + 1))
