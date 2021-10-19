t = int(input())

for _ in range(t) :
  n = bin(int(input()))[2:]
  
  for i in range(len(n)) :
    if n[::-1][i] == '1' :
      print(i, end=' ')
