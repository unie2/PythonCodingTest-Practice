a = int(input())
b = int(input())
c = int(input())

count = 0

if a == b == c == 60 :
  print("Equilateral")
elif a + b + c != 180 :
  print("Error")
else :
  if a == b :
    count += 2
  elif a == c :
    count += 2
  elif b == c :
    count += 2

  if count >= 2 :
    print("Isosceles")
  else :
    print("Scalene")
    
    
# 1. 세 각의 크기가 모두 60이면 "Equilateral"를 출력한다.
# 2. 1번 조건을 만족하지 않는 경우 수행되며, 세 각의 합이 180이 아닌 경우 "Error"를 출력한다.
# 3. 모든 조건에 만족하지 않는 경우 수행되며, 세 각의 합이 180이고, 두 각이 같은 경우 count에 2를 할당한다.
# 4. 조건문을 통해 count 값을 확인하여 2 이상일 경우 "Isosceles"를 출력한다.
# 5. 2 미만일 경우 같은 각이 없기 때문에 "Scalene"를 출력한다.
