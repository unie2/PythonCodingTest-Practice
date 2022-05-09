from copy import deepcopy

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
result = 0

def left(board) :
    for i in range(n) :
        p = 0 # 열의 가장 좌측
        x = 0
        for j in range(n) :
            if board[i][j] == 0 : # 빈칸이면 continue
                continue
            if x == 0 : # x가 비어있으면 더해줄 이전 블록이 없다는 의미이므로, x를 변경
                x = board[i][j]
            else :
                if x == board[i][j] : # 블록의 숫자가 같다면
                    board[i][p] = x * 2
                    x = 0 # 블록을 더했으므로 0으로 다시 초기화
                    p += 1 # 열에서 갈 수 있는 가장 좌측을 채웠으므로 다음 블록이 이동하기 위한 위치 증가
                else :
                    board[i][p] = x # 이동할 곳에 지난 블록 x를 저장
                    x = board[i][j] # 이전 블록을 새로운 블록으로 변경
                    p += 1 # 열에서 갈 수 있는 가장 좌측을 채웠으므로 다음 블록이 이동하기 위한 위치 증가
            board[i][j] = 0 # 블록 이동했으므로 비워줌
        if x != 0 : # 열의 우측 끝까지 도달 후에 이동할 블록이 남아있다면 블록 이동
            board[i][p] = x
    return board

def right(board) :
    for i in range(n) :
        p = n - 1 # 열의 가장 우측
        x = 0
        for j in range(n-1, -1, -1) :
            if board[i][j] == 0 : # 빈칸이면 continue
                continue
            if x == 0 : # x가 비어있으면 더해줄 이전 블록이 없다는 의미이므로 x를 변경
                x = board[i][j]
            else :
                if x == board[i][j] : # 블록의 숫자가 같다면
                    board[i][p] = x * 2
                    x = 0 # 블록을 더했으므로 0으로 다시 초기화
                    p -= 1 # 열에서 갈 수 있는 가장 우측을 채웠으므로 다음 블록이 이동하기 위한 위치 감소
                else :
                    board[i][p] = x # 이동할 곳에 지난 블록 x를 저장
                    x = board[i][j] # 이전 블록을 새로운 블록으로 변경
                    p -= 1 # 열에서 갈 수 있는 가장 우측을 채웠으므로 다음 블록이 이동하기 위한 위치 감소
            board[i][j] = 0 # 블록 이동했으므로 비워줌
        if x != 0 : # 열의 좌측 끝까지 도달 후에 이동할 블록이 남아있다면 블록 이동
            board[i][p] = x
    return board

def up(board) :
    for i in range(n) : # 열
        p = 0 # 행의 가장 위
        x = 0
        for j in range(n) :
            if board[j][i] == 0 : # 빈칸이면 continue
                continue
            if x == 0 : # x가 비어있으면 더해줄 블록이 없다는 의미이므로 x를 변경
                x = board[j][i]
            else :
                if x == board[j][i] :
                    board[p][i] = x * 2
                    x = 0
                    p += 1
                else :
                    board[p][i] = x
                    x = board[j][i]
                    p += 1
            board[j][i] = 0
        if x != 0 :
            board[p][i] = x
    return board

def down(board) :
    for i in range(n) : # 열
        p = n - 1 # 행의 가장 아래
        x = 0
        for j in range(n-1, -1, -1) :
            if board[j][i] == 0 :
                continue
            if x == 0 :
                x = board[j][i]
            else :
                if x == board[j][i] :
                    board[p][i] = x * 2
                    x = 0
                    p -= 1
                else :
                    board[p][i] = x
                    x = board[j][i]
                    p -= 1
            board[j][i] = 0
        if x != 0 :
            board[p][i] = x
    return board

def solution(board, cnt) :
    global result
    if cnt == 5 :
        for i in range(n) :
            for j in range(n) :
                result = max(result, board[i][j])
        return

    solution(left(deepcopy(board)), cnt + 1) # 블록을 좌측으로 이동
    solution(right(deepcopy(board)), cnt + 1) # 블록을 우측으로 이동
    solution(up(deepcopy(board)), cnt + 1) # 블록을 위로 이동
    solution(down(deepcopy(board)), cnt + 1) # 블록을 아래로 이동

solution(data, 0)
print(result)

'''
1. 입력받은 게임판의 초기 상태와 이동횟수를 0으로 한 값을 매개변수로 하여 solution() 함수를 호출한다.
   solution() 함수의 작업은 아래와 같다.
  - 블록을 좌측, 우측, 위, 아래로 이동하는 함수에 각 게임판의 복사본과 이동횟수(cnt)를 1 증가시킨 값을 전달하여 호출한다.
  - 이동횟수(cnt)가 5일 경우 게임판의 가장 큰 볼록을 result에 갱신한다.

2. 블록을 좌측으로 이동하는 left() 함수의 작업은 아래와 같다.
  - 게임판(board)의 현재 위치가 비어있다면 continue를 수행한다.
  - 그렇지 않다면, x 값이 비어있는지 확인하고 비어있다면 더해줄 이전 블록이 없다는 것이므로 x를 board[i][j]값으로 변경한다. 
  - x가 비어있지 않다면, x 값과 board[i][j] 값이 같은지 확인하고, 같다면 블록을 채울수 있는 가장 좌측에 x * 2 값을 할당한다.
  - 이후 블록을 더했으므로 x 값을 다시 0으로 초기화하고, 열에서 갈 수 있는 가장 좌측을 채웠으므로 다음 블록이 이동하기 위해 위치 값(p)을 1 증가시킨다.
  - 만약 x값과 board[i][j] 값이 다르다면, 이동할 곳에 지난 블록(x) 값을 할당하고 x에는 새로운 블록(board[i][j])으로 갱신한다.
     또한, 열에서 갈 수 있는 가장 좌측을 채웠으므로 다음 블록이 이동하기 위해 위치 값(p)를 1 증가시킨다.
  - 모든 열에 대한 반복 수행이 끝나면 x 값을 확인하여, 이동할 블록이 남아있다면 블록을 이동시킨다.
  - 모든 행에 대한 반복 수행이 끝나면 board 리스트를 반환한다.

3. 블록을 우측으로 이동하는 right() 함수의 작업 또한 left() 함수의 작업과 유사하며, 여기서 p는 열의 가장 우측을 의미하는 n-1을 할당해주고 열에 대한 반복문의 범위는 거꾸로 수행해준다.
   또한, 열에서 갈 수 있는 가장 우측을 채웠을 경우 다음 블록이 이동하기 위한 위치 값(p)을 1 감소시켜준다.
   
4. 블록을 상단으로 이동시키는 up() 함수의 작업 또한 left() 함수의 작업과 유사하며, 여기서는 행(j)과 열(i)을 바꿔 수행한다.

5. 블록을 하단으로 이동시키는 down() 함수의 작업 또한 right() 함수의 작업과 유사하며, 여기서는 행(j)과 열(i)을 바꿔 수행한다.

6. 최종적으로 갱신이 완료된 result 값을 출력한다.

'''
