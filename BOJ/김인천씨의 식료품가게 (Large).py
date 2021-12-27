t = int(input())
for tc in range(1, t + 1) :
  n = int(input())
  data = sorted(map(int, input().split()), reverse=True)
  result = []

  while data :
    price = data.pop()

    if price * 100//75 in data :
      result.append(str(price))
      data.remove(price * 100//75)

  print("Case #%d: %s" % (tc, " ".join(result)))
  
  
# 1. 가격을 입력받아 내림차순으로 정렬하여 data에 저장한다.
# 2. data 리스트의 원소가 빌 때까지 while문을 통해 반복수행하는데, 가장 먼저 원소를 하나 꺼내어 price에 할당한다.
# 3. price에 100//75 를 곱한 가격이 data 리스트에 존재할 경우 result 리스트에 price를 문자열로 변환하여 추가한다.
# 4. 또한, 다음 원소를 통한 조건확인이 원활하게 이루어질 수 있도록 data 리스트에서 price * 100//75 값을 제거한다.
# 5. 반복문이 종료되면 최종적으로 문제에서 요구하는 출력 형식에 맞추어 result 리스트 값들을 출력한다.
