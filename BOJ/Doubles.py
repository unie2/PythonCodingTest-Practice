while True :
  data = list(map(int, input().split()))
  if len(data) == 1 and data[0] == -1 :
    break
  
  result = 0
  for i in range(len(data)-1) :
    if data[i] % 2 == 0 :
      if data[i] // 2 in data :
        result += 1

  print(result)
  
  
# 1. 입력받은 리스트의 길이가 1이고 첫번째 원소가 -1일 때까지 while문을 통해 반복 수행한다.
# 2. 반복문을 수행하는데, 리스트의 끝인 0은 리스트에 속하지 않기 때문에 범위를 len(data)-1 로 설정한다.
# 3. data 리스트의 값을 하나씩 확인하고, 그 값이 짝수일 경우 해당 값을 2로 나눈 몫이 리스트에 존재하는지 판단한다.
# 4. 몫이 리스트에 있을 경우 result 값을 1 증가시킨다.
# 5. for문 수행이 모두 끝나면 최종적으로 result 값을 출력한다.
