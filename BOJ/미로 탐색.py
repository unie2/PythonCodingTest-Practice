# https://www.acmicpc.net/problem/2178

from collections import deque

def bfs(i, j) :
    q = deque()
    q.append((i, j))

    while q :
        x, y = q.popleft()
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < n and 0 <= ny < m) :
                continue
            if data[nx][ny] == 0 :
                continue

            if data[nx][ny] == 1 :
                data[nx][ny] = data[x][y] + 1
                q.append((nx, ny))

    return data[n-1][m-1]

n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))

'''
1. n, m, 미로의 상태판(data) 리스트를 입력받은 후 (상, 하, 좌, 우) 방향을 의미하는 dx, dy 리스트를 정의한다.

2. bfs() 함수를 호출하여 반환받은 값을 출력하는데, bfs() 함수의 작업은 아래와 같다.
  - 처음 전달받은 i, j 값 (좌표 0, 0)을 deque()에 추가한다.
  - q가 빌 때까지 수행하며, q에 존재하는 값을 꺼내 x, y에 할당한다.
  - 네 가지의 방향을 확인하는데, 각 방향마다 다음 칸을 의미하는 nx, ny를 구한다.
  - nx, ny가 범위를 벗어나거나 미로판에서의 값이 0일 경우 갈 수 없으므로 continue한다.
  - 미로판에서의 값이 1일 경우 갈 수 있으므로 해당 값을 이전 값에서 1을 더한 값으로 갱신한 뒤 q에 (nx, ny) 좌표를 추가한다.
  - q가 비면 data[n-1][m-1]의 값을 반환한다.

'''
