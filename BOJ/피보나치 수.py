data = [0] * 46

def fibo(x) :
  if x == 0 :
    return 0
  if x == 1 or x == 2 :
    return 1
  if data[x] != 0 :
    return data[x]
  data[x] = fibo(x - 1) + fibo(x - 2)
  return data[x]

n = int(input())
print(fibo(n))
