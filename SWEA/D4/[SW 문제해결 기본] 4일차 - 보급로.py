from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(data, visited, time, S, G) :
    q = deque([S]) # (0, 0) 부터 시작
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n) :
                continue
            if (nx, ny) == (0, 0) :
                continue
            if visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                time[nx][ny] = time[x][y] + data[nx][ny]
                q.append([nx, ny])
            else :
                if time[nx][ny] > time[x][y] + data[nx][ny] :
                    time[nx][ny] = time[x][y] + data[nx][ny]
                    q.append([nx, ny])

t = int(input())
for tc in range(1, t + 1) :
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    time = [[0] * n for _ in range(n)]
    S, G = (0, 0), (n-1, n-1)

    bfs(data, visited, time, S, G)
    result = time[G[0]][G[1]]

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 n x n 크기의 도로 상태를 입력받아 data 리스트에 저장한다.

2. 방문 여부를 확인할 수 있는 visited 2차원 리스트와 가장 짧은 경로에 대한 복구 시간을 담는 time 2차원 리스트를 정의한다.

3. S와 G에 각각 (0, 0)와 (n-1, n-1)을 담고, bfs() 함수를 호출하여 작업을 수행한다.

4. bfs() 작업이 모두 끝나면 최종적으로 해당 테스트 케이스 번호와 함께 G 좌표에 존재하는 값을 출력한다.

5. bfs() 함수의 작업은 아래와 같다.
  - 전달받은 S 값을 q에 할당한다.
  - q가 빌 때까지 while문을 통해 반복 작업을 수행하며, q에서 값을 빼 x, y에 할당한다.
  - 인접한 네 칸을 구하며, 각 칸(nx, ny)이 범위를 벗어나거나 좌표가 (0, 0)일 경우 continue한다.
  - 만약 (nx, ny) 위치가 아직 방문처리되지 않았다면 방문처리(1)를 하고, time[x][y] + data[nx][ny] 값을 time[nx][ny]에 할당한 후 q에 좌표를 삽입한다.
  - 방문처리되어 있다면 time[nx][ny] 값을 확인하는데, 그 값이 time[x][y] + data[nx][ny]보다 크다면 time[x][y] + data[nx][ny]로 갱신하고 q에 좌표를 삽입한다.

'''
