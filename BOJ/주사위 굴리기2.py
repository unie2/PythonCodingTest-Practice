from collections import deque
import copy

n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
ball = [2, 4, 1, 3, 5, 6] # 초기 주사위 (전면, 왼쪽, 상단, 오른쪽, 후면, 바닥)
dir = 0 # 초기 방향 (동쪽)

# 동 남 서 북 (시계 방향)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
x, y = 0, 0 # 주사위 초기 위치
result = 0 # 최종 점수

def ball_move(x, y, dir) :
    nx = x + directions[dir][0]
    ny = y + directions[dir][1]
    # 이동 방향에 칸이 없는 경우
    if check(nx, ny) :
        nd = (dir + 2) % 4
        nx = x + directions[nd][0]
        ny = y + directions[nd][1]
        return [nx, ny, nd]
    # 이동 방향에 칸이 있는 경우
    return [nx, ny, dir]


def check(nx, ny) :
    if not (0 <= nx < n and 0 <= ny < m) :
        return True
    return False

def change_ball(ball, dir) :
    # (전면, 왼쪽, 상단, 오른쪽, 후면, 바닥)
    # 동쪽 이동 (왼쪽, 상단, 오른쪽, 바닥)
    if dir == 0 :
        ball[1], ball[2], ball[3], ball[5] = ball[5], ball[1], ball[2], ball[3]
    # 남쪽 이동 (전면, 상단, 후면, 바닥)
    elif dir == 1 :
        ball[0], ball[2], ball[4], ball[5] = ball[5], ball[0], ball[2], ball[4]
    # 서쪽 이동 (왼쪽, 상단, 오른쪽, 바닥)
    elif dir == 2 :
        ball[1], ball[2], ball[3], ball[5] = ball[2], ball[3], ball[5], ball[1]
    # 북쪽 이동 (전면, 상단, 후면, 바닥)
    elif dir == 3 :
        ball[0], ball[2], ball[4], ball[5] = ball[2], ball[4], ball[5], ball[0]

    return ball

# 연속해서 이동할 수 있는 칸의 개수 조사
def bfs(x, y) :
    cnt = 1
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append([x, y])
    while q :
        r, c = q.popleft()
        visited[r][c] = 1
        for i in range(4) :
            nr = r + directions[i][0]
            nc = c + directions[i][1]
            if check(nr, nc) :
                continue
            if data[r][c] == data[nr][nc] and not visited[nr][nc] :
                visited[nr][nc] = 1
                q.append([nr, nc])
                cnt += 1

    return cnt

for _ in range(k) :
    # 주사위 이동
    x, y, dir = ball_move(x, y, dir)
    ball = change_ball(ball, dir)
    # 주사위가 도착한 칸에 대한 점수 계산
    count = bfs(x, y)
    result += data[x][y] * count

    # 주사위의 이동 방향 결정
    a, b = ball[5], data[x][y]
    # a > b 인 경우 이동 방향을 90도 시계 방향으로 회전
    if a > b :
        dir = (dir + 1) % 4
    # a < b 인 경우 이동 방향을 90도 반시계 방향으로 회전
    elif a < b :
        dir = (dir - 1)
        if dir == -1 :
            dir = 3

print(result)


'''
1. 주사위 6면의 초기 값을 ball에 정의한다. (순서는 전면, 왼쪽, 상단, 오른쪽, 후면, 바닥)

2. 초기 주사위 이동은 동쪽을 바라보고 수행하므로 dir을 0으로 초기화하고, (동 남 서 북) 순으로 directions를 정의한다.

3. 반복문 횟수는 k로 하고, 반복문 내 작업은 아래와 같다.
  - x, y(현재 주사위 좌표), dir(방향)을 매개변수로 하여 ball_move() 함수를 호출하여 x, y, dir 값을 갱신한다.
  - 값이 정의된 주사위(ball)와 방향(dir)을 매개변수로 하여 change_ball() 함수를 호출하여 ball 을 갱신한다.
  - 주사위가 도착한 칸에 대한 점수를 계산하기 위해 현재 좌표(x, y)를 매개변수로 하여 bfs() 함수를 수행하여 반환받은 값을 count에 할당한다.
  - bfs() 함수를 통해 구한 count 값을 지도 내 현재 좌표에 존재하는 값과 곱하고, result에 누적한다.
  - 주사위의 이동 방향을 결정하기 위해 주사위의 바닥면 값을 a에, 현재 주사위가 올려져 있는 지도 좌표에 설정되어 있는 값을 b에 할당한다.
  - a > b 인 경우 이동 방향을 90도 시계 방향으로 회전한다.
  - a < b 인 경우 이동 방향을 90도 반시계 방향으로 회전한다.
  
4. 주사위를 이동시키는 ball_move() 함수의 작업은 아래와 같다.
  - 설정된 방향으로 다음 좌표를 구하고 check() 함수를 통해 해당 좌표가 범위 내에 존재하는지 확인한다.
  - 범위 내에 존재하지 않는다면 방향을 바꿔 다음 좌표를 다시 구하고 해당 좌표와 방향을 반환한다.
  - (dir + 2) % 4 에서 1이 아닌 2가 더해진 이유는 현재 방향이 (동 남 서 북) 순으로 되어 있기 때문이고, (동 서 남 북) 순으로 방향을 재설정하기 위함이다.
  - 범위 내에 존재한다면 해당 좌표와 방향을 반환한다. 
  
5. 좌표가 범위 내에 존재하는지 확인하는 check() 함수의 작업은 아래와 같다.
  - 전달받은 좌표가 지도 크기를 벗어난다면 True를 반환, 그렇지 않다면 False를 반환한다.
  
6. 굴린 주사위 상태를 갱신해주기 위한 change_ball() 함수의 작업은 아래와 같다.
  - 전달받은 방향(dir) 값을 확인하여 방향에 맞게 주사위를 굴려 ball의 값을 갱신한다.
  
7. 연속해서 이동할 수 있는 칸의 개수를 구하기 위한 bfs() 함수의 작업은 아래와 같다.
  - 현재의 좌표가 연속해서 이동할 수 있는 칸의 개수에 포함되므로 cnt를 1로 초기화한다.
  - 방문여부를 확인할 수 있는 visited 리스트를 정의하고, 큐를 생성하여 현재의 좌표(x, y)를 큐에 삽입한다.
  - 큐에서 좌표를 꺼내 해당 좌표를 방문처리하고 인접한 칸의 좌표를 구한다.
  - 인접한 칸의 좌표가 지도 크기 내에 존재한다면 현재의 좌표에 존재하는 값과 같고, 아직 방문하지 않았는지 확인한다.
  - 위 조건을 만족하면 인접한 칸의 좌표를 방문처리하고 큐에 삽입한다. 이후 cnt를 1 증가시킨다.
  - 이와 같은 작업을 큐가 빌때까지 수행하고, 반복 수행이 끝나면 cnt 값을 반환한다.
  
8. 3번의 반복 작업이 모두 끝나면 최종적으로 result 값을 출력한다.

'''
