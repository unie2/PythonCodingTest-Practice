number = 1

while True :
  value = input()
  if value == '0' :
    break
  else :
    r, w, l = map(int, value.split())

    table = r * 2
    pizza = (w**2 + l**2) ** 0.5

    if table >= pizza :
      print(f"Pizza {number} fits on the table.")
    else :
      print(f"Pizza {number} does not fit on the table.")
    
    number += 1
    
    
# 1. while문 내 초기에 입력받은 값이 0이라면 반복문을 종료한다.
# 2. 0이 아닌 경우 문자열 value를 공백으로 구분하여 각 r, w, l에 값을 할당한다.
# 3. table에 식탁의 지름을 구하여 할당한다.
# 4. pizza에 피자의 대각선 길이를 구하여 할당한다.
# 5. 조건문을 통해 pizza의 값보다 table의 값이 더 크거나 같다면 크기가 맞기 때문에 문제에서 요구하는 출력형식에 맞추어서 값을 출력한다.
# 6. 그렇지 않을 경우 크기가 맞지 않기 때문에 문제에서 요구한느 출력형식에 맞추어서 값을 출력한다.
