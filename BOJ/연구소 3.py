from collections import deque
import copy

n, m = map(int, input().split())
graph = []
virus = []
result = int(1e9)
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n) :
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(n) :
        if data[j] == 2 :
            graph[i][j] = -1
            virus.append((i, j)) # 바이러스 위치

# 조합 구하는 함수
def combination(virus, count) :
    value = []
    if count > len(virus) :
        return value
    if count == 1 :
        for i in virus :
            value.append([i])
    elif count > 1 :
        for i in range(len(virus) - count + 1) :
            for j in combination(virus[i+1:], count - 1) :
                value.append(j + [virus[i]])
    return value

def bfs(temp, combi) :
    global result
    visited = [[False] * n for _ in range(n)] # 방문 처리 리스트
    q = deque()
    if check(temp) : # 빈공간 있는지 확인
        result = min(result, 0) # 빈공간이 없다면 바이러스를 퍼트릴 공간이 없으므로 0과 비교하여 최솟값으로 갱신
        return

    for c in combi :
        a, b = c
        visited[a][b] = True
        temp[a][b] = -2 # 바이러스 활성화
        q.append((a, b, 0)) # (좌표, 이동하는데 걸리는 시간)
    end_time = 0
    while q :
        x, y, time = q.popleft()
        for i in range(4) : # 인접한 네 칸에 대하여 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] :
                if temp[nx][ny] == 1 :
                    continue
                else :
                    if temp[nx][ny] == 0 :
                        end_time = max(end_time, time + 1)
                    temp[nx][ny] = -2 # 바이러스 활성화
                    visited[nx][ny] = True
                    q.append((nx, ny, time + 1))

    if check(temp) :
        result = min(result, end_time)

def check(temp) :
    for i in range(n) :
        for j in range(n) :
            if temp[i][j] == 0 : # 빈공간이 있다면 False 반환
                return False
    return True


temp = copy.deepcopy(graph)
for combi in combination(virus, m) : # 조합 구하여 BFS 작업 하기
    temp = copy.deepcopy(graph)
    bfs(temp, combi)
    temp = graph

if result == int(1e9) :
    print(-1)
else :
    print(result)
    

'''
1. 입력받은 연구소 상태 리스트에서 바이러스의 좌표를 구하여 virus 리스트에 추가한다.
2. combination() 함수를 통해 m개의 활성화 바이러스에 대한 조합을 구하여 bfs() 함수를 수행한다.
3. 우선적으로 check() 함수를 통해 빈공간 여부를 확인하는데, 빈공간이 없을 경우 바이러스를 퍼트릴 공간이 없으므로 result와 0을 비교하여 최솟값으로 갱신한다.
4. 조합을 통해 전달받은 m개의 활성화 바이러스의 위치 값을 -2로 갱신(활성화 처리)해준 뒤 방문 처리 후 큐에 (해당 좌표, 이동하는데 걸리는 시간)을 추가한다.
5. 이후 인접한 네 칸을 확인하여 각 칸의 방문처리가 되지 않았다면 방문처리를 해준 후 큐에 이동시간(time)을 1 증가시켜 추가한다.
6. 만약 해당 위치의 값이 0(빈칸)이라면 바이러스가 다 퍼져나갔을 때의 시간을 구하기 위해 end_time을 time+1과 비교하여 최댓값으로 갱신한다.
7. 이와 같은 작업을 모두 수행한 뒤 check() 함수를 통해 빈공간 여부를 확인하고, 빈 공간이 없다면 바이러스가 모두 퍼져나갔음을 의미하므로 result값을 end_time(바이러스가 다 퍼져나갔을 때의 시간) 값을 비교하여 최솟값으로 갱신한다.
8. 최종적으로 result 값을 확인하여 그 값이 int(1e9)와 같다면 바이러스를 퍼뜨릴 수 없으므로 -1을 출력하고, 그렇지 않을 경우 result값을 그대로 출력한다.

'''
