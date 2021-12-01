tc = int(input())

for _ in range(tc) :
  n = int(input())
  for i in range(n) :
    for j in range(n) :
      if i == 0 or i == n-1 :
        print('#', end='')
      else :
        if j == 0 or j == n-1 :
          print('#', end='')
        else :
          print('J', end='')
    
    print()
  print()
  
  
# 1. 이중 for문을 통해 반복문을 수행하고, 첫 번째 조건문에서 i의 값이 0이거나 마지막일 경우 '#'을 출력한다.
# 2. 그렇지 않을 경우 다시 조건문을 통해 j의 값을 확인하는데, j의 값이 0이거나 마지막을 경우 '#'을 출력한다.
# 3. 그렇지 않을 경우 'J'를 출력한다.
