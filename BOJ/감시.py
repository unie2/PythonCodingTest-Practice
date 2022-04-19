import copy

n, m = map(int, input().split())
office = []
cctv = []

case = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(depth, arr) :
    global result
    if depth == len(cctv) :
        count = 0
        for i in range(n) :
            count += arr[i].count(0)
        result = min(result, count)
        return

    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in case[cctv_num] :
        fill(temp, i, x, y)
        dfs(depth + 1, temp)
        temp = copy.deepcopy(arr)


def fill(board, index, x, y) :
    for i in index :
        nx = x
        ny = y
        while True :
            nx += dx[i]
            ny += dy[i]
            if not 0 <= nx < n or not 0 <= ny < m :
                break
            if board[nx][ny] == 6 :
                break
            elif board[nx][ny] == 0 :
                board[nx][ny] = 7

for i in range(n) :
    data = list(map(int, input().split()))
    office.append(data)
    for j in range(m) :
        if data[j] in [1, 2, 3, 4, 5] :
            cctv.append([data[j], i, j]) # [cctv 번호, 좌표]

result = int(1e9)
dfs(0, office)
print(result)

'''
1. 5가지 종류의 CCTV가 각각 감시할 수 있는 방법을 3차원 리스트 형태로 구성하여 case에 정의한다.
2. CCTV를 90도 방향으로 회전할 수 있으므로 북쪽, 동쪽, 남쪽, 서쪽 방향을 dx, dy 리스트에 정의한다.
3. 사무실 각 칸의 정보를 한 줄씩 입력받고, 그 줄의 각 요소를 확인하여 그 값이 CCTV번호라면 cctv 리스트에 [CCTV 번호, 좌표] 형태로 추가한다.
4. dfs() 함수를 통해 해당 CCTV의 방향들을 감시하고, CCTV 개수만큼 감시를 완료하면 사각지대의 최솟값을 갱신한 후 return 한다.
5. fill() 함수를 통해 해당 CCTV의 방향에 따라 감시할 수 있는 칸은 7로 갱신시키고, 벽을 만나거나 범위를 초과하면 감시를 종료한다.

'''
