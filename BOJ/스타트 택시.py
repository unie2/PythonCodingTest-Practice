from collections import deque

n, m, cost = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
car_x, car_y = map(int, input().split())
passenger = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(car_x, car_y) :
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((car_x, car_y))
    visited[car_x][car_y] = 0

    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n) :
                continue
            if data[nx][ny] == 1 or visited[nx][ny] != -1 :
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
    return visited

def check_distance(visited: list, passenger: list) :
    i = 0
    for start_x, start_y, dest_x, dest_y in passenger :
        passenger[i].append(visited[start_x-1][start_y-1])
        i += 1
    passenger.sort(key=lambda x: (-x[4], -x[0], -x[1]))

def solution(car_x, car_y) :
    global cost
    while passenger :
        visited = bfs(car_x-1, car_y-1)
        check_distance(visited, passenger)
        start_x, start_y, dest_x, dest_y, distance = passenger.pop()

        for temp in passenger :
            temp.pop()

        visited = bfs(start_x-1, start_y-1)
        distance2 = visited[dest_x-1][dest_y-1]
        car_x, car_y = dest_x, dest_y

        if distance == -1 or distance2 == -1 :
            print(-1)
            return
        cost -= distance
        if cost < 0 :
            break
        cost -= distance2
        if cost < 0 :
            break
        cost += distance2 * 2

    if cost < 0 :
        print(-1)
    else :
        print(cost)


solution(car_x, car_y)


'''
1. solution() 함수를 통해 승객의 정보(출발 행열, 목적 행열)를 하나씩 확인하며, 작업은 아래와 같다.
  - bfs() 함수를 통해 큐를 생성하여 전달받은 좌표를 큐에 삽입하고 인접한 네 방향에 대한 방문처리를 진행한다.
  - check_distance() 함수를 통해 승객 정보에 각 방문 거리를 추가하고, 최소거리, 최소행, 최소열 순으로 정렬한다.
  - 정렬된 승객의 정보를 하나씩 꺼내 출발점에서 시작한 방문처리를 진행하고, 목적지까지의 사용연료(disatnce2)를 구한다.
  - 이후 택시의 좌표를 목적지 좌표로 갱신한다.
  - 연료에서 출발점까지의 사용연료(distance)를 빼고 남은 연료가 음수라면 break 한다.
  - 연료에서 목적지까지의 사용연료(distance2)를 빼고 남은 연료가 음수라면 break 한다.
  - 남은 연료에 (목적지까지의 사용연료 * 2) 를 누적한다.
  - 최종적으로 남은 연료(cost) 값을 확인하여 음수라면 -1을 출력하고, 그렇지 않다면 남은 연료(cost) 값을 출력한다.

'''
