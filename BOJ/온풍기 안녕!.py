from copy import deepcopy
from collections import deque

# 우, 좌, 상, 하
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

r, c, k = map(int, input().split())
heater, checker = [], []
for i in range(r) :
    data = list(map(int, input().split()))
    for j in range(c) :
        if 1 <= data[j] < 5 :
            heater.append([i, j, data[j]])
        elif data[j] == 5 :
            checker.append([i, j])

w = int(input())
wall = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(w) :
    x, y, t = map(int, input().split())
    wall[x-1][y-1].append(t)

data = [[0] * c for _ in range(r)]
chocolate = 0

def func(x, y, num) :
    if visited[x][y] == 0 : # 아직 방문하지 않았다면
        visited[x][y] = 1 # 방문 처리
        data[x][y] += num # 숫자 누적
        q.append([x, y]) # 큐에 삽입

while True :
    for i, j, type in heater :
        q = deque()
        visited = [[0] * c for _ in range(r)]
        nx = i + dx[type]
        ny = j + dy[type]
        data[nx][ny] += 5

        if not (0 <= nx + dx[type] < r and 0 <= ny + dy[type] < c) :
            continue

        q.append([nx, ny])
        flag = 0
        for num in range(4, 0, -1) :
            for _ in range(len(q)) :
                x, y = q.popleft()

                if type == 1 : # 방향이 오른쪽인 온풍기
                    if y + 1 >= c : # 범위를 벗어나면
                        flag = 1
                        break
                    if 1 not in wall[x][y] : # 오른쪽에 벽이 없다면
                        nx, ny = x, y + 1
                        func(nx, ny, num)
                    if x - 1 >= 0 : # 범위 내에 있다면
                        if 0 not in wall[x][y] and 1 not in wall[x-1][y] : # 바람이 갈 수 있다면
                            nx, ny = x-1, y+1
                            func(nx, ny, num)
                    if x + 1 < r : # 범위 내에 있다면
                        if not wall[x+1][y] : # 바람이 갈 수 있다면
                            nx, ny = x+1, y+1
                            func(nx, ny, num)

                elif type == 2 : # 방향이 왼쪽인 온풍기
                    if y - 1 < 0 : # 범위를 벗어나면
                        flag = 1
                        break
                    if 1 not in wall[x][y-1] : # 바람이 갈 수 있다면
                        nx, ny = x, y-1
                        func(nx, ny, num)
                    if x-1 >= 0 : # 범위 내에 있다면
                        if 1 not in wall[x-1][y-1] and 0 not in wall[x][y] : # 바람이 갈 수 있다면
                            nx, ny = x-1, y-1
                            func(nx, ny, num)
                    if x+1 < r : # 범위 내에 있다면
                        if 1 not in wall[x+1][y-1] and 0 not in wall[x+1][y] : # 바람이 갈 수 있다면
                            nx, ny = x+1, y-1
                            func(nx, ny, num)

                elif type == 3 : # 방향이 위쪽인 온풍기
                    if x-1 < 0 : # 범위를 벗어난다면
                        flag = 1
                        break
                    if 0 not in wall[x][y] :
                        nx, ny = x-1, y
                        func(nx, ny, num)
                    if y-1 >= 0 : # 범위 내에 있다면
                        if not wall[x][y-1] : # 바람이 갈 수 있다면
                            nx, ny = x-1, y-1
                            func(nx, ny, num)
                    if y+1 < c : # 범위 내에 있다면
                        if 0 not in wall[x][y+1] and 1 not in wall[x][y] : # 바람이 갈 수 있다면
                            nx, ny = x-1, y+1
                            func(nx, ny, num)

                else : # 방향이 아래쪽인 온풍기
                    if x+1 >= r :
                        flag = 1
                        break
                    if 0 not in wall[x+1][y] :
                        nx, ny = x+1, y
                        func(nx, ny, num)
                    if y-1 >= 0 :
                        if 0 not in wall[x+1][y-1] and 1 not in wall[x][y-1] :
                            nx, ny = x+1, y-1
                            func(nx, ny, num)
                    if y+1 < c :
                        if 1 not in wall[x][y] and 0 not in wall[x+1][y+1] :
                            nx, ny = x+1, y+1
                            func(nx, ny, num)

            if flag == 1 or len(q) == 0 :
                break

    temp = deepcopy(data)
    for x in range(r) :
        for y in range(c) :
            direction = []
            if x < r-1 and 0 not in wall[x+1][y] :
                direction.append(4)
            if 1 not in wall[x][y] :
                direction.append(1)

            for d in direction :
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < r and 0 <= ny < c :
                    if data[x][y] > data[nx][ny] :
                        diff = (data[x][y] - data[nx][ny]) // 4
                        temp[x][y] -= diff
                        temp[nx][ny] += diff
                    elif data[x][y] < data[nx][ny] :
                        diff = (data[nx][ny] - data[x][y]) // 4
                        temp[x][y] += diff
                        temp[nx][ny] -= diff

    data = temp
    for i in range(r) :
        if i == 0 or i == r-1 :
            for j in range(c) :
                if data[i][j] > 0 :
                    data[i][j] -= 1
        else :
            for j in [0, c-1] :
                if data[i][j] > 0 :
                    data[i][j] -= 1

    chocolate += 1
    if chocolate > 100 :
        break

    flag = 0
    for x, y in checker :
        if data[x][y] < k :
            flag = 1
            break
    if flag == 0 :
        break

print(chocolate)


'''
1. 온풍기의 번호는 1~4이며, 순서대로 오른쪽, 왼쪽, 위, 아래 방향의 온풍기로 제시하였으므로 같은 순서로 dx, dy를 정의한다.

2. 방의 정보를 입력받아 온풍기의 좌표와 번호를 heater 리스트에 담고, 조사해야 하는 칸이면 해당 좌표를 checker 리스트에 담는다.

3. 벽의 정보를 입력받아 해당 좌표를 인덱스로 하여 3차원 배열 wall에 방향 값을 담는다.

4. 먹은 초콜릿의 개수가 100을 초과하거나 조사하는 모든 칸의 온도가 k 이상이 되었을 때까지 while문을 통해 아래와 같이 반복 수행한다.
  - 큐를 생성하고 방문 여부를 확인할 수 있는 visited 리스트를 정의한다.
  - 온풍기의 방향으로 한 칸 이동한 좌표를 구해 해당 좌표에 5를 누적한다.
  - 그 다음 좌표가 범위를 벗어난다면 continue를 수행한다.
  - 범위 내에 있다면, 큐에 좌표를 삽입하고, 큐에서 좌표를 하나씩 꺼내 가야하는 좌표에 갈 수 있는지 확인하여 갈 수 있다면 func() 함수를 통해 방문처리를 해주고 값을 누적한 후 큐에 삽입한다.
  - 만약 각 방향에서 다음 좌표로 이동할 수 없다면 flag 값을 1로 갱신하고 break를 수행한다.
  - flag값이 1이거나 큐가 비어 있으면 문제에서 제시한 1번 과정을 마치고 2번 과정을 수행한다.
 
  - 1번 과정을 마치면, 온도 조절 작업을 수행하고 임시 temp 리스트를 통해 온도가 동시에 조절될 수 있도록 한다.
  - 온도 조절 작업을 마치면 data 리스트를 temp 리스트 상태로 갱신한다.
 
  - 이후 반복문을 통해 온도가 1 이상인 가장 바깥쪽 칸의 온도를 1씩 감소시키고 chocolate 값을 1 증기시킨다.
  - 마지막 단계로 checker의 원소를 확인해 조사하는 모든 칸의 온도가 k 이상이 되었는지 검사하고, 모든 칸의 온도가 k 이상이 아니라면 위 과정을 다시 반복한다.

'''
