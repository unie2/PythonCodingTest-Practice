while True :
  data = list(map(int, input().split()))
  if data[0] == 0 and data[1] == 0 and data[2] == 0 :
    break
  
  data.sort(reverse=True)
  if data[0] >= data[1] + data[2] :
    print("Invalid")
  else :
    if data[0] == data[1] == data[2] :
      print("Equilateral")
    elif data[0] == data[1] or data[0] == data[2] or data[1] == data[2] :
      print("Isosceles")
    else :
      print("Scalene")
      
      
# 입력받은 세 수가 모두 0일때까지 while문을 수행하며, 그 내부에서는 입력받은 세 수를 리스트 형태로 구성하고 
# 내림차순으로 값들을 정렬한다. 정렬한 후에는 조건문을 통해 data리스트에서의 최댓값이 나머지 두 값의 합보다 
# 크거나 같을 경우 삼각형의 조건을 만족하지 못하기 때문에 "Invalid"를 출력한다.
# 삼각형의 조건을 만족한다면 다시 조건문을 통해 세 수를 확인하고 아래와 같이 만족하는 조건에 따라 출력한다.
# 1. 세변의 길이가 모두 같은 경우 "Equilateral"을 출력한다.
# 2. 두 변의 길이만 같은 경우 "Isosceles"를 출력한다.
# 3. 세 변의 길이가 모두 다른 경우 "Scalene"을 출력한다.
