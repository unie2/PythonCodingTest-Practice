# https://www.acmicpc.net/problem/2583

from collections import deque

n, m, k = map(int, input().split())
data = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []
for _ in range(k) :
    sy, sx, ey, ex = map(int, input().split())
    ey -= 1
    ex -= 1
    for i in range(sx, ex + 1) :
        for j in range(sy, ey + 1) :
            data[i][j] = 1

def bfs(r, c) :
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    count = 1

    while q :
        x, y = q.popleft()
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < n and 0 <= ny < m) :
                continue
            if data[nx][ny] == 1 :
                continue
            elif data[nx][ny] == 0 and visited[nx][ny] == False :
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1

    return count

# 분리 영역 구하기
for i in range(n) :
    for j in range(m) :
        if data[i][j] == 0 and visited[i][j] == False :
            result.append(bfs(i, j))

result.sort()
print(len(result))
print(* result)


'''
1. 입력받은 크기만큼의 2차원 data 리스트와 방문여부를 확인할 수 있는 2차원 visited 리스트, (상, 하, 좌, 우) 방향을 담은 dx, dy 리스트를 정의한다.
 
2. 개인적으로 편리하게 리스트를 정의하기 위해 (시작점y, 시작점x, 끝점y, 끝점x) 순으로 값을 입력받는다. 즉, 문제에서 제시한 그림의 상하 반전으로 표현된다.
 
3. 끝점의 경우 입력받은 값을 그대로 사용하면 index out of range가 발생하므로 1을 감소시킨다.
 
4. 이후 입력받은 좌표로 구성되는 직사각형 모양의 값들을 1로 갱신한다.
 
5. k개의 작업을 완료한 후 분리 영역을 구하는데, 한 칸씩 확인하여 그 값이 0이고 아직 방문하지 않았다면 bfs() 함수를 호출하여 반환받은 값을 result리스트에 추가한다.
 
6.bfs() 함수의 작업은 아래와 같다.
  - deque()를 정의하여 (r, c) 값을 q에 할당하고 방문 처리를 해준 뒤 해당 영역에 존재하는 칸의 개수를 위해 count를 1로 초기화 한다.
  - q가 빌 때까지 좌표를 하나씩 꺼내 각 방향에 대한 다음 좌표(nx, ny)를 구한다.
  - 다음 좌표가 범위를 벗어나거나 data[nx][ny] 값이 1일 경우 continue한다.
  - 그렇지 않고 data[nx][ny] 값이 0이고 아직 방문하지 않았다면 방문처리를 해주고 q에 좌표 값을 추가한 뒤 count를 1 증가시킨다.
  - while문이 종료되면 count 값을 반환한다.
 
7. 최종적으로 result 리스트를 오름차순으로 정렬한 후 result 리스트에 존재하는 요소의 개수와 값들을 출력한다.

'''
