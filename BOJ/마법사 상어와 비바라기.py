n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

move = []
for i in range(m) :
    temp = list(map(int, input().split()))
    move.append([temp[0] - 1, temp[1]])

for i in range(m) :
    # 1단계
    moving = move[i]
    next_cloud = []
    for c in cloud :
        x = c[0]
        y = c[1]
        d, s = moving[0], moving[1]
        nx = (n + x + dx[d] * s) % n
        ny = (n + y + dy[d] * s) % n
        next_cloud.append([nx, ny])

    # 2단계
    visited = [[False] * n for _ in range(n)]
    for drop in next_cloud :
        x = drop[0]
        y = drop[1]
        data[x][y] += 1
        visited[x][y] = True

    # 3단계
    cloud = []

    # 4단계
    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]
    for j in next_cloud :
        x = j[0]
        y = j[1]
        count = 0
        for k in range(4) :
            nx = x + cx[k]
            ny = y + cy[k]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] >= 1 :
                count += 1
        data[x][y] += count

    # 5단계
    for j in range(n) :
        for k in range(n) :
            if data[j][k] >= 2 and visited[j][k] == False :
                data[j][k] -= 2
                cloud.append([j, k])


# 최종
result = 0
for i in range(n) :
    result += sum(data[i])

print(result)

'''
1. 비바라기를 시전했을 시 생기는 비구름의 위치를 2차원 리스트 형태로 구성하여 cloud에 저장한다.
2. 구름이 이동하는 8개의 방향을 문제에서 제시한 순서대로 정의하여 각 dx, dy에 저장한다.
3. 입력받은 이동 방향과 거리를 move 리스트에 추가하는데, 방향의 경우 인덱스를 맞춰주기 위해 1 감소시킨 값으로 저장한다. 
4. 1단계 : 반복문을 통해 모든 구름이 d 방향으로 s칸 이동한다.
5. 2단계 : 방문처리 여부를 담을 수 있는 visited리스트를 정의하고, 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양을 1 증가시킨다. 이후 해당 칸을 방문처리한다.
6. 3단계 : cloud 리스트를 빈 리스트로 재정의 해줌으로써 구름을 모두 제거한다.
7. 4단계 : 대각선 위치(cx, cy)를 정의하고, 해당 대각선 위치에 물이 있는 바구니의 수(count)를 세어 기존 위치에 있는 바구니의 물의 양을 count만큼 증가시킨다.
8. 5단계 : 바구니에 저장된 물의 양이 2 이상이고 방문처리 되지 않았을 경우에만 물의 양을 2 감소시키고, 해당 좌표를 cloud 리스트에 추가한다.
9. 위 작업을 m번 만큼 반복 수행하고, 모두 마치면 최종적으로 data 리스트의 값을 통해 바구니에 들어있는 물의 양의 합을 구하여 출력한다.

'''
