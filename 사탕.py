t = int(input())
for _ in range(t) :
  j, n = map(int, input().split())

  data = []
  for _ in range(n) :
    a, b = map(int, input().split())
    data.append(a*b)

  data.sort(reverse=True)
  result = 0
  for i in range(len(data)) :
    j -= data[i]
    result += 1
    if j <= 0 :
      break

  print(result)
  
  
# 1. 상자의 세로 길이와 가로 길이를 입력받아 각각 a와 b에 할당한다.
# 2. a와 b를 곱해 data 리스트에 추가한 후 상자의 개수를 최소한으로 구해야하므로 내림차순으로 정렬한다.
# 3. 반복문을 통해 data 리스트의 값을 하나씩 확인하면서 사탕의 개수에서 현재 확인하고 있는 상자의 크기를 빼고 result를 1증가시킨다.
# 4. 만약 사탕의 개수가 0이하일 경우 더 이상 상자에 넣을 사탕이 없으므로 반복문을 종료한다.
# 5. 최종적으로 result 값을 출력한다.
