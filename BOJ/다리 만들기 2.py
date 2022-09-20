# https://www.acmicpc.net/problem/17472

from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
land = dict()
landArr = []

number = 0
for i in range(n) :
    for j in range(m) :
        if data[i][j] == 1 and visited[i][j] == False :
            q = deque([(i, j)])
            visited[i][j] = True
            land[(i, j)] = number
            landArr.append((i, j, number))

            while q :
                x, y = q.popleft()
                for r, c in move :
                    nx = x + r
                    ny = y + c
                    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and data[nx][ny] == 1 :
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        land[(nx, ny)] = number
                        landArr.append((nx, ny, number))
            number += 1

edges = []
for x, y, fromLand in landArr : # 좌표, 섬 번호
    for r, c in move :
        dist = 0
        nx = x + r
        ny = y + c
        while True :
            if not (0 <= nx < n and 0 <= ny < m) :
                break
            toLand = land.get((nx, ny))
            # 같은 번호의 섬일 경우
            if fromLand == toLand :
                break
            # 바다 위일 경우
            if toLand == None :
                nx = nx + r
                ny = ny + c
                dist += 1
                continue
            # 다리 길이가 2보다 작을 경우
            if dist < 2 :
                break

            edges.append((dist, fromLand, toLand)) # 섬과 섬 간의 거리
            break

edges = sorted(edges, reverse=True)

result = 0
count = number - 1
parents = [i for i in range(number)]
flag = 0

def find(k) :
    if k != parents[k] :
        parents[k] = find(parents[k])
    return parents[k]

def union(x, y) :
    x = find(x)
    y = find(y)
    parents[y] = x

# print(edges)
while count :
    try :
        distance, a, b = edges.pop() # 거리가 작은 것부터 pop
    except :
        flag = 1
        break

    if find(a) != find(b) :
        union(a, b)
        result += distance
        count -= 1

if flag == 1 :
    print(-1)
else :
    print(result)
    
'''
1. 지도의 상태를 입력받고,방문여부 체크를 위한  n x m 크기의 2차원 visited 리스트, (동, 남, 서, 북) 방향의 move 리스트,
    각 좌표가 포함하는 섬 번호를 정의하기 위한 land 딕셔너리, 각 좌표와 섬 번호를 함께 담을 landArr 리스트를 정의한다.

2. 지도의 각 칸을 하나씩 확인하여 그 값이 1이고 아직 방문하지 않았다면 해당 좌표를 q에 할당하고 방문처리를 한 후 섬의 번호를 부여한다.

3. q가 빌때까지 아래와 같은 작업을 반복하고, 반복 수행이 모두 끝나면 섬 번호(number)를 1 증가시킨다.
  - q에서 좌표를 꺼내 x, y에 담고 move 리스트를 기반으로 다음 좌표를 구한다.
  - 다음 좌표가 범위 내에 존재하고 아직 방문하지 않았고, 지도에 존재하는 해당 좌표의 값이 1일 경우 q에 해당 좌표를 추가 및 방문처리를 하고, 섬의 번호를 부여한다.

4. 정의된 landArr 리스트에서 각 좌표(x, y)와 섬의 번호(fromLand)를 기반으로 아래와 같은 작업을 수행한다.
  - move 리스트를 기반으로 다음 좌표를 구하고, 만약 해당 좌표가 범위를 벗어나면 break하여 다음 방향을 확인한다.
  - break 되지 않았다면 해당 좌표의 섬 번호를 가져와 toLand에 할당한다.
  - 만약 fromLand(원래 섬의 번호)와 toLand(다음 좌표의 섬 번호)가 같을 경우 같은 섬이므로 break한다.
  - 만약 toLand가 None일 경우 섬이 아니라 바다 위이므로 다음 좌표를 구한 뒤 dist를 1증가시킨 후 continue한다.
  - 만약 continue되지 않고 dist값이 2보다 작을 경우 다리를 연결할 수 없으므로 break한다.
  - break되지 않았다면 다리정보를 의미하는 edges리스트에 (거리, 원래 섬, 다음 섬) 정보를 추가하고 break한다.

5. 다리 정보가 담겨있는 edges 리스트를 내림차순으로 정렬한다.

6. while문 내부의 작업은 아래와 같다.
  - 거리가 작은 것부터 정보를 빼내어 각 distance, a, b에 할당하는데, 더 이상 꺼낼 수 없을 경우 flag 값을 1로 갱신하고 break한다.
  - 각 a와 b 값에 대한 find() 함수의 반환 값이 다를 경우 union() 함수를 수행하고 result 값에 distance를 누적한 뒤 count를 1 감소시킨다.

7. flag값이 1일 경우 -1을 출력하고, 그렇지 않다면 result 값을 출력한다.

** find() 함수는 특정 원소가 속한 집합을 찾는 함수이며, union() 함수는 두 원소가 속한 집합을 합치는 함수이다.

## 참고 ##
https://unie2.tistory.com/302
https://my-coding-notes.tistory.com/352
'''
