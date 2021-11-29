data = list(map(int, input().split()))
target = [1, 2, 3, 4, 5]

while data != target :
  for i in range(4) :
    if data[i] > data[i+1] :
      data[i], data[i+1] = data[i+1], data[i]
    else :
      continue
    for j in range(5) :
      print(data[j], end=' ')
    print()
    
    
# 1. 나무 조각을 1, 2, 3, 4, 5 순서로 만들기 위해 target 리스트를 생성한다.
# 2. while문을 통해 입력받은 나무 조각 값들이 1, 2, 3, 4, 5 순서로 될때까지 반복 수행한다.
# 3. for문을 통해 현재의 값과 다음 값을 비교하고 현재의 값이 더 크면 둘의 위치를 서로 바꾼다.
# 4. 현재의 값이 더 작을 경우 continue를 통해 다음 값 확인으로 넘어간다.
# 5. for문을 통해 변경된 data 리스트를 출력한다.
