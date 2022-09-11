''' Case 1 - DFS 방식 '''
def dfs(x, y) :
    global count

    if not (0 <= x < n and 0 <= y < n) :
        return False

    if data[x][y] == 1 :
        count += 1
        data[x][y] = 0

        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            dfs(nx, ny)

        return True
    return False


n = int(input())
data = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = 0
result = []

count = 0
for i in range(n) :
    for j in range(n) :
        if dfs(i, j) == True :
            total += 1
            result.append(count)
            count = 0

print(total)
result.sort()
for res in result :
    print(res)
    

'''
1. 지도 상태를 입력받아 data 리스트에 저장하고, (상, 하, 좌, 우) 방향을 담은 dx, dy 리스트를 정의한다.

2. 지도의 각 칸의 상태를 확인하여 dfs() 함수를 호출하고, 반환받은 값이 True일 경우 total을 1 증가시키고, count 값을 result 리스트에 할당한 뒤 count 값을 다시 0으로 초기화한다.

3. 모든 칸에 대한 방문이 끝나면 최종적으로 total과 오름차순으로 정렬된 result 리스트의 값들을 하나씩 출력한다.

4. dfs() 함수의 작업은 아래와 같다.
  - 만약 전달받은 좌표(x, y)가 범위를 벗어나지 않고 data[x][y]가 1일 경우 해당 값을 0으로 갱신해주고 count 값을 1 증가시킨다.
  - 이후 네 가지의 방향에 대한 각 좌표 값을 구하여 dfs() 함수에 전달함으로써 재귀호출을 수행한다.
  - 네 가지 방향에 대하여 모두 확인한 뒤 True를 반환한다.
  - 만약 data[x][y]의 값이 1이 아닐 경우 False를 반환한다.

'''


''' Case 2 - BFS 방식 '''
from collections import deque

def bfs(i, j) :
    global data

    q = deque()
    q.append((i, j))
    data[i][j] = 0

    cnt = 1
    while q :
        x, y = q.popleft()
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < n and 0 <= ny < n) :
                continue

            if data[nx][ny] == 1 :
                data[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1

    return cnt

n = int(input())
data = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = 0
result = []

for i in range(n) :
    for j in range(n) :
        if data[i][j] == 1 :
            total += 1
            count = bfs(i, j)
            result.append(count)

print(total)
result.sort()
for res in result :
    print(res)
    
'''
1. DFS 방식과 마찬가지로 지도의 상태와 네 가지 방향을 담은 dx, dy 리스트를 정의한다.

2. 지도의 각 칸을 확인하여 그 값이 1일 경우 total을 1 증가시키고, bfs() 함수를 호출하여 반환받은 값을 result 리스트에 추가한다.

3. 모든 칸에 대한 확인을 마치면 최종적으로 total과 오름차순으로 정렬된 result 리스트의 값들을 하나씩 출력한다.

4. bfs() 함수의 작업은 아래와 같다.
  - deque를 정의하여 전달받은 좌표(i, j)를 q에 추가한 후 해당 좌표의 값을 0으로 갱신한다.
  - q가 빌 때까지 좌표를 하나씩 꺼내 x, y에 담고, 네 가지 방향에 대한 각 방향의 좌표(nx, ny)를 구한다.
  - 만약 해당 좌표(nx, ny)가 범위를 벗어나지 않고 지도에 담긴 값이 1일 경우 해당 좌표의 값을 0으로 갱신해주고 q에 해당 좌표를 추가한 뒤 cnt 값을 1 증가시킨다.
  - q에 담긴 값들에 대한 처리를 모두 끝낸 후 cnt 값을 반환한다.

'''
