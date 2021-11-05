day = int(input())
car = list(map(int, input().split()))

count = 0

for i in range(len(car)) :
  if car[i] == day :
    count += 1

print(count)


# 5대의 자동차 번호의 일의 자리 숫자를 리스트 형태로 담아 반복문을 통해 리스트에 담겨 있는 값을 하나씩 확인하면서
# 해당 번호가 입력받은 날짜의 일의 자리 숫자(day)와 일치하다면 10부제를 위반하는 차량이므로 count를 1 증가시킨다.
