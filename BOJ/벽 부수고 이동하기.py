from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b, c) :
    q = deque()
    q.append((a, b, c))

    while q :
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1 :
            return visited[x][y][z]

        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < n and 0 <= ny < m) :
                continue
            # 다음 좌표가 벽이고, 벽 파괴 X
            if data[nx][ny] == 1 and z == 0 :
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append((nx, ny, 1))
            # 다음 좌표가 벽이 아니고, 방문하지 않았다면
            elif data[nx][ny] == 0 and visited[nx][ny][z] == 0 :
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))

    return -1

print(bfs(0, 0, 0))

'''
1. 벽 파괴 가능 여부를 담은 visited 3차원 리스트를 정의하고 visited[0][0][0] 을 1로 갱신한다.

2. (n-1, m-1) 좌표로 가기 위해 (상, 하, 좌, 우) 방향을 담은 dx, dy 리스트를 정의한다.

3. (0, 0) 좌표부터 시작하므로 bfs(0, 0, 0) 을 호출하여 반환받은 값을 출력한다. bfs() 함수의 작업은 아래와 같다.
  - deque()를 정의하여 전달받은 매개변수(a, b, c)를 q에 추가한다.
  - q가 빌 때까지 x, y, z 를 꺼내고, 만약 (n-1, m-1) 좌표에 도달했을 경우 visited[x][y][z] 값을 반환한다.
  - 네 가지의 방향을 확인하는데, 각 방향으로의 다음 좌표 값이 범위를 벗어난다면 continue 한다.
  - 범위를 벗어나지 않고, 다음 좌표가 벽이고 벽 파괴를 하지 않은 경우 visited[nx][ny][1]에 현재의 visited[x][y][0]에 1을 더한 값을 할당한 후 q에 추가한다.
  - 그렇지 않고 다음 좌표가 벽이 아니고, 아직 방문하지 않았다면 방문 처리를 해준 뒤 q에 추가한다.
  - q가 빌 때까지 return 되지 않았다면 (n-1, m-1) 좌표로 도달할 수 없으므로 -1을 반환한다.

'''
