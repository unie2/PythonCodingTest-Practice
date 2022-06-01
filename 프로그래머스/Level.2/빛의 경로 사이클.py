# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(x, y, dir, pos) :
    if pos == 'L' : # 좌로 가는데 L을 만나면 하, 우로 가는데 L을 만나면 상
        dir = (dir - 1) % 4
    elif pos == 'R' :
        dir = (dir + 1) % 4

    nx = (x + dx[dir]) % row
    ny = (y + dy[dir]) % col

    return nx, ny, dir

def solution(grid) :
    answer = []
    global row, col
    row = len(grid)
    col = len(grid[0])
    visited = [[[False] * 4 for _ in range(col)] for _ in range(row)]

    for i in range(row) :
        for j in range(col) :
            for k in range(4) : # 네 방향에 대하여 확인
                if not visited[i][j][k] :
                    route = 0
                    x, y, dir = i, j, k

                    while not visited[x][y][dir] :
                        route += 1
                        visited[x][y][dir] = True
                        x, y, dir = move(x, y, dir, grid[x][y])

                    answer.append(route)

    answer.sort()
    return answer
  
'''
1. (상 우 하 좌) 순으로 방향 정보를 담은 dx, dy를 정의하고, 네 방향에 대한 방문 여부를 확인하기 위해 visited 리스트를 정의한다.

2. 한 칸에 대하여 각 방향을 확인하는데, 해당 칸의 특정 방향을 방문하지 않았다면 방문처리를 해준 뒤 move() 함수를 통해 올바른 칸으로 이동한다.

3. move() 함수의 작업은 아래와 같다.
  - 좌로 이동하는데 'L'을 만나면 하로 이동하고, 우로 이동하는데 'L'을 만나면 상으로 이동할 수 있도록 방향 정보를 갱신한다.
  - 갱신된 방향으로 한 칸 이동 하여 해당 좌표와 방향을 반환한다.

4. 반환받은 좌표와 방향을 x, y, dir에 갱신하면서 사이클이 발생하면 while문을 종료하고 answer 리스트에 while문이 수행된 횟수를 저장한다.

5. 모든 칸에 대하여 확인 작업이 끝나면 answer 리스트를 오름차순으로 정렬하여 반환한다.

'''
