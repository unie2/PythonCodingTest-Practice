month = int(input())
day = int(input())

if month == 2 :
  if day == 18 :
    print('Special')
  elif day < 18 :
    print('Before')
  else :
    print('After')
elif month < 2 :
  print('Before')
else :
  print('After')
  
  
# 1. 날짜가 2월 18일이라면 "Special"을 출력한다.
# 2. 날짜가 2월 18일 전이면 "Before"을 출력한다.
# 3. 날짜가 2월 18일 후면 "After"을 출력한다.
