data = []

for _ in range(8) :
  data.append(list(map(str, list(input()))))

result = 0

for i in range(8) :
  for j in range(8) :
    if (i+j) % 2 == 0 :
      if data[i][j] == 'F' :
        result += 1

print(result)


# 8x8 크기의 체스판에 입력하는 값들이 들어갈 수 있도록 리스트 형태로 구성한다.
# 이중 for문을 통해 반복문을 수행하며, 조건문을 통해 i + j의 값이 짝수일 경우 하얀 칸이기 때문에 현재 확인하고 있는
# 인덱스의 값이 'F'인지 확인한다. 'F'일 경우 말이 존재하는 것이기 때문에 result 값을 1 증가시킨다.
# 반복문이 종료되면 최종적으로 result 값을 출력한다.
