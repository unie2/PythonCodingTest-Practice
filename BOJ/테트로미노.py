# Case 1
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
max_value = 0

# 테트로미노 좌표 정보 (기준점은 가장 왼쪽 + 위쪽에 위치한 정사각형)
case = [
    # case 1 (ㅡ, ㅣ)
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    # case 2 (ㅁ)
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    # case 3 (ㄴ 회전 및 대칭)
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [0, 1], [0, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 2]],
    [[0, 0], [0, 1], [-1, 1], [-2, 1]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    # case 4 (회전 및 대칭)
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [-1, 1], [-1, 2]],
    [[0, 0], [0, 1], [-1, 1], [1, 0]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    # case 5 (ㅜ, ㅓ, ㅗ, ㅏ)
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [-1, 1], [0, 1], [1, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 1]],
    [[0, 0], [1, 0], [2, 0], [1, 1]]
]

def tetromino(i, j) :
    for x in range(19) :
        sum_value = 0
        for y in range(4) :
            try :
                sum_value += board[i + case[x][y][0]][j + case[x][y][1]]
            except :
                break
        check(sum_value)

def check(sum_value) :
    global max_value
    max_value = max(max_value, sum_value)

for i in range(n) :
    for j in range(m) :
        tetromino(i, j)

print(max_value)

'''
1. 5가지 테트로미노의 각 회전 및 대칭 모양을 3차원 배열 형태로 case에 정의한다.
2. 각 자리를 기준으로 tetromino() 함수를 호출하여 테트로미노가 놓인 칸에 쓰인 수들의 합을 구한다.
3. check() 함수를 호출하여 더 큰 값을 max_value에 갱신하고, tetromino() 함수의 작업이 모두 끝나면 최종적으로 max_value 값을 출력한다.

'''

# Case 2
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 최대값 변수
max_value = 0

# ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
def dfs(i, j, dsum, cnt) :
    global max_value
    # 모양 완성되었을 때 최대값 계산
    if cnt == 4 :
        max_value = max(max_value, dsum)
        return

    # 상, 하, 좌, 우로 이동
    for k in range(4) :
        nx = i + move[k][0]
        ny = j + move[k][1]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] :
            # 방문 표시 및 제거
            visited[nx][ny] = True
            dfs(nx, ny, dsum + data[nx][ny], cnt + 1)
            visited[nx][ny] = False

# ㅗ, ㅜ, ㅓ, ㅏ 모양의 최대값 계산
def exce(i, j) :
    global max_value
    for k in range(4) :
        # 초기값은 시작지점의 값으로 지정
        temp = data[i][j]
        for l in range(3) :
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (k + l) % 4
            nx = i + move[t][0]
            ny = j + move[t][1]

            if not (0 <= nx < n and 0 <= ny < m) :
                temp = 0
                break
            temp += data[nx][ny]
        # 최대값 계산
        max_value = max(max_value, temp)

for i in range(n) :
    for j in range(m) :
        # 시작점 visited 표시
        visited[i][j] = True
        dfs(i, j, data[i][j], 1)
        visited[i][j] = False

        exce(i, j)

print(max_value)

'''
1. 'ㅜ' 모양을 제외하고 나머지 4개의 모양들은 연달아 이을 수 있으므로 4개의 모양에 대한 처리와 'ㅜ'모양에 대한 처리를 따로 진행한다.
2. 4개의 모양에 대한 처리 함수 dfs() 의 작업은 아래와 같다.
 - 정의한 move 배열의 요소들을 통해 상, 하, 좌, 우 좌표를 구하여 방문 처리를 진행하고 dfs() 함수를 재귀호출하여 모양이 완성되었을 때 최대값을 갱신한다.
 - 재귀호출 후에는 방문처리한 좌표를 다시 False로 갱신해준다.
3. 'ㅜ' 모양에 대한 처리 함수 exce() 의 작업은 아래와 같다.
 - 초기값은 시작지점의 값으로 지정하고 move 배열의 요소를 3개씩 사용할 수 있도록 하여 각 좌표를 구해 범위를 벗어나지 않는다면 temp에 data[nx][ny] 값을 누적한다.
 - 이후 max_value와 temp 값을 확인하여 최대 값을 구해 max_value에 갱신한다.

'''
