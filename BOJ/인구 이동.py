from collections import deque

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index) :
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    # 너비 우선 탐색(BFS)을 위한 큐 자료구조 정의
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수

    # 큐가 빌 때까지 반복(BFS)
    while q :
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1 :
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r :
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))

    # 연합 국가끼리 인구를 분배
    for i, j in united :
        graph[i][j] = summary // count
    return count

# 땅의 크기, L, R 값을 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보를 입력받기
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
day = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True :
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n) :
        for j in range(n) :
            if union[i][j] == -1 : # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1

    # 모든 인구 이동이 끝난 경우
    if index == n * n :
        break
    day += 1

print(day)


'''
1. 땅의 크기(n), L, R의 값을 입력받고, 전체 나라의 정보(graph)를 입력받아 리스트 형태로 구성한다.
2. 인접한 국가를 확인하기 위해 상, 좌, 하, 우 위치를 의미하는 dx, dy를 정의한다.
3. 더 이상 인구 이동을 할 수 없을 때까지 반복하는데, 연합 국가 정보를 확인하기 위해 union 리스트를 구성한다.
4. union리스트의 값을 하나씩 확인하여 그 값이 아직 처리되지 않았다면(-1) process() 함수를 호출하고 index를 1 증가시킨다.
5. process() 함수에서는 전달받은 위치와 연결된 나라(연합) 정보를 담는 리스트를 구성한다.
6. 너비 우선 탐색(BFS)을 위한 큐 자료구조를 정의하고 현재 연합의 번호와 현재 연합의 전체 인구 수를 각각 union[x][y]과 summary에 할당한다.
  또한, 현재 연합의 국가 수를 의미하는 count 값의 초기 값은 1로 지정한다.
7. 큐가 빌 때까지 반복 수행하는데, 특정 위치를 큐에서 꺼내 네 가지 방향을 확인하여 각각 인접한 나라와 인구 차이를 확인한다.
8. 인구 차이가 L명 이상 R명 이하라면 연합에 추가하는 작업을 진행한다.
9. 연합 구성 작업을 모두 마치면 연합 국가끼리 인구를 분배하여 count 값을 반환한다.
10. 이러한 인구 이동 작업을 진행할 때마다 day 값을 1씩 증가시켜주고, 모든 인구 이동이 끝나면 최종적으로 day 값을 출력한다.

'''
