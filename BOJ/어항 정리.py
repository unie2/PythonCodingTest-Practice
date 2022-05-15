# 1. 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다.
# 2. 가장 왼쪽에 있는 어항을 그 어항의 오른쪽에 있는 어항의 위에 올리기
# 3. 행이 2 이상이면, 시계방향으로 90도 회전 후 어항 위에 올리기
# 4. 바닥에 있는 어항의 범위보다 초과되면 안됌
# 5. 물고기의 수를 조절 : 동시에 발생
# 6. 어항을 다시 일렬로 놓기
# 7. 반으로 나눠 왼쪽 부분을 180도 회전 -> 2번 반복
# 8. 다시 물고기의 수를 조절
# 9. 바닥에 일렬로 놓기

from collections import deque

n, k = map(int, input().split())
# 상 하 좌 우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = [deque(list(map(int, input().split())))]

result = 0

def get_diff(board) :
    get_q = board[0]
    return max(get_q) - min(get_q)

def rotate_stack(arr) :
    while True :
        if len(arr) > len(arr[0]) - len(arr[-1]) :
            break
        blocks = []
        r = len(arr)
        c = len(arr[-1])

        for i in range(r) :
            temp_q = deque()
            for _ in range(c) :
                temp_q.append(arr[i].popleft())
            blocks.append(temp_q)

        arr = [arr[0]]
        rotated = rotate_90(blocks)
        for row in rotated :
            arr.append(deque(row))

    return arr


def rotate_90(block) :
    temp = [[0] * len(block) for _ in range(len(block[0]))]
    for i in range(len(block[0])) :
        for j in range(len(block)) :
            temp[i][j] = block[j][len(block[0])-1-i]
    return temp

def fix_fish(arr) :
    dp = [[0] * len(arr[x]) for x in range(len(arr))]
    for x in range(len(arr)) :
        for y in range(len(arr[x])) :
            for dir in directions :
                nx = x + dir[0]
                ny = y + dir[1]

                if 0 <= nx < len(arr) and 0 <= ny < len(arr[nx]) :
                    # 현재 칸이 인접한 칸보다 크면
                    if arr[x][y] > arr[nx][ny] :
                        diff = (arr[x][y] - arr[nx][ny]) // 5
                        if diff >= 1 :
                            dp[x][y] -= diff
                    else : # 현재 칸이 인접한 칸보다 작으면
                        diff = (arr[nx][ny] - arr[x][y]) // 5
                        if diff >= 1 :
                            dp[x][y] += diff
    for i in range(len(arr)) :
        for j in range(len(arr[i])) :
            arr[i][j] += dp[i][j]

def make_one_line(arr) :
    temp = deque()
    for i in range(len(arr[-1])) :
        for j in range(len(arr)) :
            temp.append(arr[j][i])

    for i in range(len(arr[-1]), len(arr[0])) :
        temp.append(arr[0][i])

    return [temp]

def half_rotation(arr) :
    temp = deque()
    for i in range(n // 2) :
        temp.append(arr[0].popleft())
    rotated = rotate_180([temp])
    arr += rotated

    left = []
    for i in range(2) :
        data = deque()
        for j in range(n // 4) :
            data.append(arr[i].popleft())
        left.append(data)
    rotated = rotate_180(left)
    arr += rotated

def rotate_180(arr) :
    temp = []
    for i in reversed(range(len(arr))) :
        arr[i].reverse()
        temp.append(arr[i])

    return temp


while True :
    # 물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이 구하기
    diff = get_diff(board)
    if diff <= k :
        print(result)
        break

    # 1번 수행
    min_value = min(board[0])
    for i in range(len(board[0])) :
        if board[0][i] == min_value :
            board[0][i] += 1

    # 2번 수행
    value = board[0].popleft()
    board.append(deque([value]))
    # 3번 수행
    board = rotate_stack(board)
    # 5번 수행
    fix_fish(board)
    # 6번 수행
    board = make_one_line(board)
    # 7번 수행
    half_rotation(board)
    # 8번 수행
    fix_fish(board)
    # 9번 수행
    board = make_one_line(board)

    result += 1
    
'''
1. 물고기의 수를 조절하는 작업에서 사용될 방향 (상 하 좌 우)을 정의하여 directions 리스트에 저장한다.

2. deque() 를 통해 어항 상태를 입력받아 구성하고, 물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수의 차이가 k 이하가 될 때까지 아래와 같은 작업을 반복 수행한다.
  - (1번 수행) 어항에서 가장 작은 값을 가져와 min_value에 할당하고, 각 어항을 확인하여 어항에 들어있는 물고기의 수가 min_value와 같다면 1 증가시킨다.
  - (2번 수행) 가장 좌측에 있는 어항을 빼내고 value에 할당한 후 deque() 로 감싸 다시 board 리스트에 추가한다.
  - (3번 수행) rotate_stack() 함수를 통해 board 리스트를 시계 방향으로 90도 회전시킨 후 바닥에 있는 어항 위에 쌓는다.
  - (5번 수행) fix_fish() 함수를 통해 물고기의 수를 조절한다. 주의할 점은 조절하는 작업이 동시에 이루어지므로 board 리스트를 그대로 다루지 않고 임시 리스트를 통해 수행해야 한다.
  - (6번 수행) make_one_line() 함수를 통해 어항(board)을 일렬로 만들어준다.
  - (7번 수행) half_rotate() 함수를 통해 n개의 어항을 반으로 나눠 왼쪽 부분을 180도 회전하는 작업을 2번 해준다.
  - (8번 수행) fix_fish() 함수를 통해 다시 물고기의 수를 조절해준다.
  - (9번 수행) make_one_line() 함수를 통해 다시 board 리스트를 바닥에 일렬로 놓아준다.
  - 9번 수행까지 완료하면 어항 정리 횟수(result)를 1 증가시킨다.
  - 물고기의 수의 차이가 k 이하가 되면 result 값을 출력하고 반복 작업을 종료한다.
  
3. 리스트를 시계 방향으로 90도 회전시킨 후 바닥에 있는 어항 위에 쌓는 rotate_stack() 함수의 작업은 아래와 같다.
  - 전달받은 arr 리스트의 행이 회전되는 칸을 제외한 바닥에 있는 어항의 길이보다 클 경우 가장 오른쪽에 있는 어항의 아래에 바닥에 있는 어항이 없게 되므로 break 한다.
  - 위 조건이 아닐 경우, 회전 시킬 칸을 빼내어 temp_q 리스트에 추가한다.
  - 한 줄의 어항들을 빼낼 때마다 blocks 리스트에 temp_q 리스트를 추가한다.
  - rotate_90() 함수를 통해 정의된 blocks 리스트를 90도 시계 방향으로 회전시킨다.
  - 회전된 리스트 rotated 에서 행을 하나씩 가져와 arr 리스트에 추가하고, while문이 종료되면 arr 리스트를 반환한다.

4. 물고기의 수를 조절하는 fix_fish() 함수의 작업은 아래와 같다.
  - 임시 리스트(dp)를 정의한다.
  - 각 위치에서 인접한 네 방향을 확인하여 현재 칸이 인접한 칸보다 크면 두 어항에 대해서 물고기 수의 차이를 5로 나눈 몫을 구해 현재 칸에 있는 물고기 수에서 뺀다.
  - 반대로 만약 현재 칸이 인접한 칸보다 작으면 인접한 칸의 어항에 있는 물고기 수에서 뺀다.
  - 모든 위치가 인접한 칸의 위치를 확인하여 물고기의 수를 갱신하는 작업을 마치면 arr[i][j] 위치에 dp[i][j] 값을 더한다.

5. 어항을 일렬로 놓아주는 make_one_line() 함수의 작업은 아래와 같다.
  - arr 리스트의 마지막 행에 대한 열의 크기를 열로, arr 리스트의 행의 크기를 행으로 설정하여 temp에 arr[j][i]를 추가한다.
  - 이후 바닥에 남아있는 어항(arr[0][i])도 temp 리스트에 추가해준다. 작업을 마치면 [temp] 를 반환한다.

6. 어항을 반으로 나누는 half_totation() 함수와 180도 돌리는 rotate_180() 함수의 작업은 아래와 같다.
  - 반복문을 통해 arr 리스트의 가장 왼쪽 요소를 n // 2 개 빼내어 temp에 추가한다.
  - rotate_180() 함수를 통해 n // 2 개의 요소를 180도 회전시켜준다. 
  - arr 리스트에 회전이 완료된 rotated 리스트를 추가한다.
  - 다시 n // 4 로 나눠 180도 회전하여 arr 리스트에 회전이 완료된 left 리스트를 추가한다.

'''
