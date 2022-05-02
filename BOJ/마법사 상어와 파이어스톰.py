from collections import deque

n, q = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(2 ** n)]
l = list(map(int, input().split()))
max_l = max(l)
temp = [[0 for _ in range(2 ** max_l)] for _ in range(2 ** max_l)]
visited = [[0 for _ in range(2 ** n)] for _ in range(2 ** n)]
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

def rotate(position, l) :
    cur_r, cur_c = position

    for r in range(l) :
        for c in range(l) :
            temp[r][c] = data[cur_r+l-1-c][cur_c+r]

    for r in range(l) :
        for c in range(l) :
            data[cur_r+r][cur_c+c] = temp[r][c]

def visitable(nr, nc) :
    return 0 <= nr < 2 ** n and 0 <= nc < 2 ** n and data[nr][nc]

def simulation(l_value) :
    # 격자 크기 만큼 90도 회전
    for r in range(0, 2 ** n, l_value) :
        for c in range(0, 2 ** n, l_value) :
            rotate((r, c), l_value)

    check = [[0 for _ in range(2 ** n)] for _ in range(2 ** n)]

    # 인접한 얼음이 3개 미만인 경우 찾기
    for r in range(2 ** n) :
        for c in range(2 ** n) :
            if not data[r][c] :
                continue

            count = 0
            for dr, dc in directions :
                nr = r + dr
                nc = c + dc
                if visitable(nr, nc) :
                    count += 1

            # check 하지 않고 바로 녹이게 되면 탐색에 영향을 받음
            if count < 3 :
                check[r][c] = 1

    # 찾은 얼음 녹이기
    for r in range(2 ** n) :
        for c in range(2 ** n) :
            if check[r][c] :
                data[r][c] -= 1

def bfs(start) :
    q = deque([start])
    cnt = 1

    while q :
        cur_r, cur_c = q.popleft()
        for dr, dc in directions :
            nr = cur_r + dr
            nc = cur_c + dc

            if visitable(nr, nc) and not visited[nr][nc] :
                visited[nr][nc] = 1
                q.append((nr, nc))
                cnt += 1
    return cnt

for cur_l in l :
    simulation(2 ** cur_l)

# 남아 있는 얼음의 총합
sum_ice = sum(sum(data, []))
# 남아 있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
max_ice = 0
for i in range(2 ** n) :
    for j in range(2 ** n) :
        if data[i][j] and not visited[i][j] :
            visited[i][j] = 1
            max_ice = max(max_ice, bfs((i, j)))

print(sum_ice)
print(max_ice)


'''
1. 아래와 같은 변수들을 정의한다.
  - 각 칸의 얼음의 양이 담겨 있는 (2 ** n) x (2 ** n) 크기의 data 리스트
  - 입력받은 단계(l) 값 중 가장 큰 값 max_l
  - 각 격자를 회전시키는 작업에 사용될 임시 temp 리스트
  - 덩어리가 차지하는 칸의 개수를 구하는 작업에 사용될 방문처리 여부 visited 리스트
  - 인접한 네 칸의 좌표를 의미하는 directions

2. 입력받은 l의 값을 하나씩 확인하여 simuation() 함수를 호출한다. sumulation() 함수의 작업은 아래와 같다.
  - rotate() 함수를 호출하여 격자 크기만큼 90도를 회전한다.
  - 인접한 얼음이 3개 미만인 경우를 찾는데, 인접한 칸이 범위 내에 있고 얼음이 있을 경우 count를 1씩 증가시킨다.
  - 인접한 칸을 모두 확인하고 누적된 count 값이 3 미만일 경우 check 리스트의 해당 좌표 값을 1로 갱신한다.
  - 위 작업이 끝나면 check 리스트 값을 확인하고, 찾은 얼음을 녹인다 (1 감소)
  
3. data 리스트의 값들을 모두 더하여 남아 있는 얼음의 총합(sum_ice)을 구한다.

4. bfs() 함수를 호출하여 남아 있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수를 구한다. bfs() 함수의 작업은 아래와 같다.
  - 전달받은 좌표를 큐에 삽입하고 덩어리가 차지하는 칸의 개수(cnt)를 1로 초기화 한다.
  - 큐가 빌 때까지 수행되며, 큐에서 좌표를 꺼내 인접한 칸을 확인하여 visitable() 함수에 만족하고 방문처리가 되지 않은 경우에 방문 처리를 수행(1로 갱신)한다.
  - 또한, 인접한 칸의 좌표를 큐에 삽입한 후 cnt 값을 1 증가시킨다.
  - 이와 같은 작업을 모두 마치면 cnt 값을 반환한다.
  
5. 최종적으로 남아 있는 얼음의 총합(sum_ice) 값과 남아 있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수(max_ice)를 출력한다.

'''
