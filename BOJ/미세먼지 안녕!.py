r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
front = 0
back = 0

# 공기 청정기 위치 확인
for i in range(r) :
    if room[i][0] == -1 :
        front = i
        back = i + 1
        break

# 미세먼지 확산
def spread() :
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    temp = [[0] * c for _ in range(r)]
    for i in range(r) :
        for j in range(c) :
            if room[i][j] != 0 and room[i][j] != -1 :
                value = 0
                for k in range(4) :
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1 :
                        temp[nx][ny] += room[i][j] // 5
                        value += room[i][j] // 5
                room[i][j] -= value
    for i in range(r) :
        for j in range(c) :
            room[i][j] += temp[i][j]

# 위쪽 공기청정기 동작
def air_up() :
    # 반시계 방향 (동 북 서 남)
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = front, 1
    while True :
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == front and y == 0 :
            break
        if not 0 <= nx < r or not 0 <= ny < c :
            direct += 1
            continue
        room[x][y], before = before, room[x][y]
        x, y = nx, ny

# 아래쪽 공기청정기 동작
def air_down() :
    # 시계 방향 (동 남 서 북)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = back, 1
    while True :
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == back and y == 0 :
            break
        if not 0 <= nx < r or not 0 <= ny < c :
            direct += 1
            continue
        room[x][y], before = before, room[x][y]
        x, y = nx, ny

for _ in range(t) :
    spread()
    air_up()
    air_down()

result = 0
for i in range(r) :
    for j in range(c) :
        if room[i][j] > 0 :
            result += room[i][j]

print(result)

'''
1. 공기 청정기의 위치를 확인하여 위쪽에 해당하는 위치를 front에 할당하고, 아래쪽에 해당하는 위치를 위쪽 위치에 1을 더하여 back에 할당한다.
2. 입력받은 t만큼 반복하여 미세먼지 확산 함수(spread()), 위쪽 공기청정기 동작 함수(air_up()), 아래쪽 공기청정기 동작 함수(air_down())를 수행한다.
3. spread() 함수에서는 인접한 네 칸을 확인할 수 있도록 dx, dy를 구성하고, R*C 크기의 temp 리스트를 생성한다.
4. 반복문을 통해 room 리스트의 요소를 하나씩 확인하여 해당 위치에 미세먼지가 존재한다면 인접한 네 칸에 대하여 미세먼지를 확산시킨다.
5. 확산되는 양은 (기준 값 // 5) 이며, 기준 값에서 (기준 값 // 5)을 확산된 방향의 개수만큼 감소시킨다.
6. air_up() 함수에서는 공기청정기의 바람이 반시계 방향으로 동작하므로 (동 북 서 남) 순서로 dx, dy를 구성한다.
7. 반복문을 통해 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동시키고, 공기청정기 좌표에 도달하면 반복문을 빠져나온다.
8. air_down() 함수에서는 공기청정기의 바람이 시계 방향으로 동작하므로 (동 남 서 북) 순서로 dx, dy를 구성하고, air_up() 함수와 마찬가지로 공기청정기를 동작시킨다.
9. 이와 같은 작업을 t만큼 반복수행하고, 최종적으로 방에 남아있는 미세먼지의 양을 result 값에 누적시켜 출력한다.

'''
