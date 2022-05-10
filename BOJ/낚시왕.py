r, c, m = map(int, input().split())
# 위 아래 오른쪽 왼쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
result = 0

data = [[[] for _ in range(c)] for _ in range(r)]

for _ in range(m) :
    x, y, s, d, z = map(int, input().split())
    data[x-1][y-1].append([z, s, d - 1])

def moving() :
    temp = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r) :
        for j in range(c) :
            if data[i][j] : # 상어가 존재한다면
                x, y = i, j
                z, s, d = data[i][j][0]
                speed = s
                while speed > 0 :
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if not (0 <= nx < r and 0 <= ny < c) : # 방향 전환
                        if d in [0, 2] : # 위 혹은 오른쪽일 경우
                            d += 1 # 아래 혹은 왼쪽으로 방향 전환
                        elif d in [1, 3] : # 아래 혹은 왼쪽일 경우
                            d -= 1 # 위 혹은 오른쪽으로 방향 전환
                        continue
                    else : # 이동할 칸이 존재한다면
                        x, y = nx, ny
                        speed -= 1
                temp[x][y].append([z, s, d])

    for i in range(r) :
        for j in range(c) :
            data[i][j] = temp[i][j]

for j in range(c) :
    for i in range(r) :
        if data[i][j] : # 상어가 존재한다면
            value = data[i][j][0]
            result += value[0] # 상어 크기를 result에 누적
            data[i][j].remove(value) # 잡은 상어는 제거
            break

    moving()

    for k in range(r) :
        for l in range(c) :
            if len(data[k][l]) >= 2 : # 한 칸에 상어가 2마리 이상일 경우
                data[k][l].sort(reverse=True) # 내림차순으로 정렬
                while len(data[k][l]) >= 2 :
                    data[k][l].pop() # 크기가 작은 상어들 제거

print(result)


'''
1. 문제에서 제시한 이동방향을 정의하기 위해 (북, 남, 동, 서) 순으로 dx, dy 를 구성한다.

2. m개의 상어 정보를 입력받아 각 data 리스트의 해당 위치(data[x-1][y-1])에 크기(z), 속력(s), 이동 방향(d-1)을 삽입한다.

3. data 리스트 요소를 하나씩 확인하여 해당 위치에 상어가 존재한다면 result에 해당 상어의 크기를 더하고, 낚시왕이 해당 상어를 잡았으므로 해당 상어 정보를 제거한다.

4. 한 마리의 상어를 잡은 후 moving() 함수를 수행한다. moving() 함수의 작업은 아래와 같다.
  - 임시 리스트 temp를 생성하고 data 리스트 요소를 하나씩 확인하여 해당 위치에 상어가 존재한다면 해당 상어가 갖고 있는 속력이 0이 될때까지 반복 작업을 수행한다.
  - 반복 작업 내에서는 다음에 이동할 좌표(nx, ny)를 구하고 그 좌표가 범위를 벗어난다면 방향을 전환한다.
  - 만약 범위를 벗어나지 않는다면 상어를 그 좌표에 이동시키고 속력(speed)을 1 감소시킨다.
  - 모든 속력에 대하여 반복 작업 처리가 끝나면 임시 리스트(temp) 내 해당 좌표에 상어의 크기(z), 속력(s), 이동 방향(d)을 삽입한다.
  - 이후 모든 상어에 대한 이동을 마치면 data 리스트 요소를 temp 리스트 요소로 갱신한다.
  
5. moving() 함수 작업을 마치면 data 리스트 요소를 한씩 확인하고, 해당 위치에 상어가 두 마리 이상 존재하면 내림차순으로 정렬하여 크기가 작은 상어들을 제거한다.

6. 이와 같은 작업을 모두 마치면 최종적으로 낚시왕이 잡은 상어 크기의 합(result)을 출력한다.

'''
