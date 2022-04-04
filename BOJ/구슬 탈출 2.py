from collections import deque

n, m = map(int, input().split())
board = []
for i in range(n) :
    board.append(list(input()))
    for j in range(m) :
        if board[i][j] == 'R' : # 빨간구슬의 위치
            rx, ry = i, j
        elif board[i][j] == 'B' : # 파란구슬의 위치
            bx, by = i, j

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, bx, by) :
    q = deque()
    q.append((rx, ry, bx, by))
    visited = [] # 방문 처리 리스트
    visited.append((rx, ry, bx, by))
    count = 0

    while q :
        for _ in range(len(q)) :
            rx, ry, bx, by = q.popleft()
            if count > 10 : # 움직인 횟수가 10회 초과면 -1 출력
                print(-1)
                return
            if board[rx][ry] == 'O' : # 빨간 구슬이 구멍에 들어가면 count를 출력
                print(count)
                return

            for i in range(4) : # 네 가지 방향으로 탐색
                nrx, nry = rx, ry # 빨간 구슬
                while True :
                    nrx += dx[i]
                    nry += dy[i]
                    if board[nrx][nry] == '#' : # 벽일 경우 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if board[nrx][nry] == 'O' :
                        break

                nbx, nby = bx, by # 파란 구슬
                while True :
                    nbx += dx[i]
                    nby += dy[i]
                    if board[nbx][nby] == '#' : # 벽일 경우 한칸 뒤로 이동
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if board[nbx][nby] == 'O' :
                        break

                if board[nbx][nby] == 'O' : # 파란구슬이 먼저 구멍에 들어갔을 경우 무시
                    continue
                if nrx == nbx and nry == nby : # 두 구슬의 위치가 같을 경우
                    # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬을 한칸 뒤로 이동
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by) :
                        nrx -= dx[i]
                        nry -= dy[i]
                    else :
                        nbx -= dx[i]
                        nby -= dy[i]

                if (nrx, nry, nbx, nby) not in visited : # 방문하지 않았다면 방문 처리
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    print(-1)

bfs(rx, ry, bx, by)

'''
1. 초기에 빨간 구슬의 위치와 파란 구슬의 위치를 각각 구해 rx, ry, bx, by에 할당한다.
2. 상 하 좌 우 방향을 정의하고, 반복문을 통해 구슬이 '#' 이나 'O'에 도달할 때까지 이동시킨다.
3. 파란 구슬이 먼저 구멍에 들어가거나 빨간 구슬과 동시에 들어갈 수 없으므로 무시한다.
4. 두 구슬의 위치가 같다면 더 많이 이동한 구슬을 한칸 뒤로 이동시킨다.
5. 이동시킨 빨간구슬, 파란구슬의 위치가 방문처리 되지 않았다면 큐에 추가하고 방문처리를 해준다.
6. 위치를 이동시키는 작업을 한번 할때마다 count를 1증가시키고, count 값이 10을 초과할 경우 -1을 출력한다.
7. 현재 빨간 구슬의 위치가 구멍('O')이라면 count를 출력하고 return 한다.


'''
