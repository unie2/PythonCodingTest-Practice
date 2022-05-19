from collections import deque

def bfs(arr, x, y) :
    q = deque()
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q.append((x, y))

    while q :
        cx, cy = q.popleft()
        for i in range(4) :
            nx = cx + dx[i]
            ny = cy + dy[i]
            if not (0 <= nx < len(arr) and 0 <= ny < len(arr[0])) :
                continue
            if arr[nx][ny] == 0 :
                continue
            if arr[nx][ny] == 1 :
                arr[nx][ny] = arr[cx][cy] + 1
                q.append((nx, ny))

    return arr

def solution(maps) :
    bfs(maps, 0, 0)
    if maps[len(maps)-1][len(maps[0])-1] == 1 :
        return -1
    else :
        return maps[len(maps)-1][len(maps[0])-1]
      
'''
1. 최단거리를 구하는 bfs() 함수의 작업은 아래와 같다.
  - 큐를 생성하여 전달받은 현재 좌표(0, 0)를 삽입하고, (동 남 서 북) 방향을 담은 dx, dy를 정의한다.
  - 큐가 빌 때까지 큐에서 좌표를 꺼내고 해당 위치에서 인접한 네 칸의 좌표를 확인한다.
  - 인접한 칸이 범위를 벗어나거나 벽(0)일 경우 continue를 수행한다.
  - 인접한 칸이 길(1)일 경우 인접한 칸에 원래 좌표의 값에 1을 더하여 할당하고, 큐에 인접한 좌표를 삽입한다.

2. bfs() 함수를 통한 거리 갱신 작업을 마치면 게임 맵의 우측 하단(상대방 진영)을 확인하여 그 값이 1일 경우 갈 수 없으므로 -1을 반환하고, 그렇지 않다면 해당 위치의 값을 반환한다.

'''
