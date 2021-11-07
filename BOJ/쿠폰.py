tc = int(input())

for _ in range(tc) :
  n = float(input())
  discount = n * (20/100)
  print("$%.2f" % (n - discount))
  
  
# 입력받은 n의 가격에서 20%의 가격을 구한다. (discount)
# 출력 시 원래의 가격(n)에서 할인가격(discount)를 뺀 값을 구하여 소수점 둘째 자리까지 출력한다.
