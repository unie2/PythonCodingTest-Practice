data = [[1 for _ in range(i)] for i in range(1, 31)]

for i in range(2, 30) :
  for j in range(1, i) :
    data[i][j] = data[i-1][j-1] + data[i-1][j]

n, k = map(int, input().split())
print(data[n-1][k-1])


# 리스트 형태로 파스칼의 삼각형을 구성하고 반복문을 통해 바로 위 행의 인접한 두 수의 합으로 갱신한다.
# 최종적으로 n과 k를 입력받아 n-1행의 k-1번째 값을 출력한다.
