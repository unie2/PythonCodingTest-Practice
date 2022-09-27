# https://www.acmicpc.net/problem/2636

from collections import deque

def bfs() :
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append([0, 0])
    visited[0][0] = True
    count = 0

    while q :
        x, y = q.popleft()
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < n and 0 <= ny < m) :
                continue
            if visited[nx][ny] == False :
                if data[nx][ny] == 0 :
                    visited[nx][ny] = True
                    q.append([nx, ny])
                elif data[nx][ny] == 1 :
                    data[nx][ny] = 0
                    visited[nx][ny] = True
                    count += 1

    cheese_cnt.append(count)
    return count


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
cheese_cnt = []

while True :
    cnt = bfs()
    if cnt == 0 :
        break
    time += 1

print(time)
print(cheese_cnt[-2])


'''
1. 각 좌표의 (상, 하, 좌, 우) 방향의 좌표를 확인하기 위해 dx, dy 리스트를 정의한다.
 
2. 격자판에 존재하는 치즈의 개수가 0이 될 때까지 while문을 반복 수행하며, 그 내부에서는 bfs()함수를 수행하고 시간(time)을 1 증가시킨다.
 
3. bfs() 함수의 작업은 아래와 같다.
  - 방문 여부를 확인할 수 있는 2차원 visited 리스트를 정의한다.
  - deque()를 정의하고 (0, 0) 좌표 값을 q에 추가한 후 방문 처리를 해준다.
  - q가 빌 때까지 q에서 좌표를 하나 꺼내고 네 가지 방향에 대하여 확인하는데, 각 방향의 다음 좌표 값이 격자판 범위를 벗어난다면 continue한다.
  - 범위를 벗어나지 않는다면 해당 좌표의 방문 여부를 확인하고, 만약 아직 방문하지 않았고 치즈가 없는 칸이라면 방문 처리를 해준 뒤 q에 (nx, ny) 좌표를 추가한다.
  - (nx, ny) 좌표를 아직 방문하지 않았고 치즈가 있는 칸이라면 해당 좌표의 값을 0으로 갱신해주고 방문 처리를 해준 뒤 count 값을 1 증가시킨다.
 
  - while문 작업이 종료되면 cheese_cnt 리스트에 치즈의 개수(count)를 추가하고 count 값을 반환한다.
 
4. 최종적으로 while문이 종료되면 time 값과 치즈가 모두 녹기 한 시간 전에 남아있는 치즈조각의 개수(cheese_cnt[-2])를 출력한다.

'''
