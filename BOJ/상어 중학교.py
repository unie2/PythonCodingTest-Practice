from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

result = 0

def bfs(x, y, num) :
    q = deque()
    q.append([x, y])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    block_cnt, rainbow = 1, 0 # 블록 개수, 무지개블록 개수
    block_list, rainbow_list = [[x, y]], [] # 블록좌표 리스트, 무지개블록 좌표 리스트

    while q :
        x, y = q.popleft()
        for dir in range(4) :
            nx = x + dx[dir]
            ny = y + dy[dir]

            # 범위 내에 존재하고 방문하지 않은 동일한 종류의 블록이라면
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and data[nx][ny] == num :
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                block_list.append([nx, ny])
            # 범위 내에 존재하고 방문하지 않은 무지개 블록이라면
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and data[nx][ny] == 0 :
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                rainbow += 1
                rainbow_list.append([nx, ny])
    # 무지개 블록은 다시 방문 해제 (다른 블록 그룹을 위해)
    for r, c in rainbow_list :
        visited[r][c] = 0

    return [block_cnt, rainbow, block_list + rainbow_list]

def remove_block(arr) :
    for r, c in arr :
        data[r][c] = -2 # 제거 처리

def gravity(arr) :
    for i in range(n-2, -1, -1) : # 밑에서부터 수행
        for j in range(n) :
            if arr[i][j] > -1 :
                r = i
                while True :
                    if 0 <= r + 1 < n and arr[r+1][j] == -2 : # 범위 내에 존재하고 빈 칸이라면
                        arr[r+1][j] = arr[r][j]
                        arr[r][j] = -2
                        r += 1
                    else :
                        break

def rotation_90(arr) :
    temp = [[0] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            temp[n-1-j][i] = arr[i][j]

    return temp

while True :
    # 크기가 가장 큰 그룹 찾기
    visited = [[0] * n for _ in range(n)] # 방문 처리 리스트
    blocks = [] # 가능한 블록 그룹 리스트
    for i in range(n) :
        for j in range(n) :
            if data[i][j] > 0 and not visited[i][j] : # 일반블록이면서 방문 안했다면
                visited[i][j] = 1 # 방문 처리
                block_info = bfs(i, j, data[i][j]) # 인접한 블록 찾기 (일반블록 개수, 무지개 개수, 블록 좌표)

                if block_info[0] >= 2 :
                    blocks.append(block_info)
    # 내림차순 정렬 (가장 큰 그룹 도출)
    blocks.sort(reverse=True)

    # 블록 제거 및 점수 획득
    if not blocks :
        break
    remove_block(blocks[0][2])
    result += blocks[0][0] ** 2

    # 중력 작용
    gravity(data)
    # 90도 반시계 방향 회전
    data = rotation_90(data)
    # 다시 중력 작용
    gravity(data)

print(result)


'''
1. N x N 크기의 격자 상태를 입력받아 data 리스트에 정의하고, 그룹이 없을 때까지 오토플레이를 수행해야 하므로 while문을 통해 아래와 같이 작업한다.
  - 크기가 가장 큰 그룹을 찾는 과정에서 일반블록과 무지개 블록의 방문 여부를 확인할 수 있도록 visited 리스트를 정의한다.
  - 블록 그룹들을 넣어줄 blocks 리스트를 정의한다.
  - data 리스트의 요소를 하나씩 확인하며, 그 값이 0보다 크고(일반블록), 아직 방문하지 않았다면 방문처리를 해주고 bfs() 함수를 통해 인접한 블록을 찾아준다.
  - 찾은 블록 정보를 block_info에 할당하고 해당 정보에서 블록의 개수(block_info[0])가 2 이상일 경우에만 blocks 리스트에 추가한다.
  - 그룹을 찾는 작업이 끝나면 가장 큰 그룹을 도출하기 위해 blocks 리스트를 내림차순으로 정렬한다.
  - remove_block() 함수를 통해 블록을 제거한 후 점수(result)에 (블록의 개수**2) 값을 누적한다.
  - gravity() 함수를 통해 중력 작업을 수행하고 rotation_90() 함수를 통해 data 리스트를 90도 반시계 방향으로 회전한 후 다시 중력 작업을 수행한다.
  - 위 작업을 반복하고, 만약 blocks 리스트에 요소가 없다면 break 한 후 최종적으로 result 값을 출력한다.
  
2. bfs() 함수의 작업은 아래와 같다.
  - 인접한 칸(상 우 하 좌)을 확인하기 위해 dx, dy 리스트를 정의한다.
  - 전달받은 좌표(x, y)를 큐에 삽입하고, 블록의 개수(block_cnt), 무지개 블록의 개수(rainbow)를 각 1과 0으로 초기화해준 후 블록좌표를 넣을 block_list, 무지개좌표를 넣을 rainbow_list를 정의한다.
  - 큐가 빌 때까지 큐에서 해당 좌표를 꺼내 인접한 칸의 좌표(nx, ny)를 도출한다.
  - 인접한 칸의 좌표가 범위 내에 존재하고 방문하지 않은 동일한 종류의 블록이라면 방문처리를 해주고 큐에 좌표를 삽입한다.
  - 이후 블록의 개수(block_cnt)를 1 증가시킨 후 block_list에 좌표를 추가한다.
 
  - 만약 인접한 칸의 좌표가 범위 내에 존재하고 방문하지 않은 무지개 블록이라면 방문처리를 해주고 큐에 좌표를 삽입한다.
  - 이후 블록의 개수(block_cnt)와 무지개 블록의 개수를 1 증가시킨 후 rainbow_list에 좌표를 추가한다.
 
  - 큐에 대한 작업이 끝나면 무지개 블록의 좌표에 대한 방문처리를 다시 해제한다.
  - [블록의 개수, 무지개 블록의 개수, 블록좌표 리스트 + 무지개블록 좌표 리스트] 를 반환한다.
  
3. 블록을 제거하는 remove_block() 함수의 작업은 아래와 같다.
  - 전달받은 리스트에서 좌표를 꺼내 해당 위치의 값을 -2로 갱신하여 제거 처리를 수행한다.

4. 중력 작용을 수행하는 gravity() 함수의 작업은 아래와 같다.
  - 전달받은 리스트의 요소를 아래부터 확인하여 그 값이 -1보다 클 경우(무지개 블록 혹은 일반 블록) 행이 큰 쪽으로 한 칸씩 이동시켜준다.

5. 격자 상태를 90도 반시계 방향으로 회전시킬 수 있는 rotation_90() 함수의 작업은 아래와 같다.
  - 임시 temp 리스트를 생성하고, 전달 받은 리스트의 요소를 90도 반시계 방향의 위치의 temp 리스트에 넣어준다.
  - 모든 요소를 90도 반시계 방향으로 회전하는 작업을 마치면 temp 리스트를 반환한다.

'''
