n, k = map(int, input().split())

data = []
for i in range(1, k + 1) :
  value = str(n * i)
  data.append(int(value[-1::-1]))
  
print(max(data))


# 1. 반복문을 통해 k개 항의 값을 바탕으로 구구단 값을 구해 value에 할당한다.
# 2. value의 값을 거꾸로 배치하여 정수형으로 변환한 뒤 data 리스트에 추가한다.
# 3. 반복문이 종료되면 최종적으로 data리스트에서 가장 큰 값을 출력한다.
