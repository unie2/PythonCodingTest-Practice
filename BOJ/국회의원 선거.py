n = int(input())
dasom = int(input())
if n <= 1 :
  print(0)
else :
  others = []
  for _ in range(n-1) :
    others.append(int(input()))

  result = 0
  while max(others) >= dasom :
    data = others.index(max(others))
    dasom += 1
    others[data] -=1
    result += 1

  print(result)
  
  
# 1. n과 다솜이의 득표수를 입력받은 후, 입력받은 n이 1 이하일 경우 0을 출력한다.
# 2. 1 이상일 경우 다솜이의 득표수는 이미 입력받았기 때문에 n-1명만큼의 각 득표수를 입력받아 others리스트에 추가한다.
# 3. 다솜이의 득표수가 최대값이 될 때까지 while문을 통해 반복수행한다.
# 4. 반복문 내부에서는 others리스트 중 최대값을 가지는 인덱스를 구하고 해당 인덱스의 득표수를 다솜이에게 준다. 그 후 result를 1 증가시킨다.
# 5. 반복문이 끝나면 최종적으로 result 값을 출력한다.
