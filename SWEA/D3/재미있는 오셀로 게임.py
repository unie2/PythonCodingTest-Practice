t = int(input())

direction = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
for tc in range(1, t + 1) :
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]

    mid = n // 2
    board[mid][mid] = 2 # 백
    board[mid-1][mid-1] = 2 # 백
    board[mid-1][mid] = 1 #흑
    board[mid][mid-1] = 1 #흑

    for i in range(m) :
        x, y, t = map(int, input().split())
        x, y = x-1, y-1

        data = []
        for i in range(8) :
            dx, dy = direction[i]
            nx = x + dx
            ny = y + dy
            while True :
                if not (0 <= nx < n and 0 <= ny < n) :
                    data = []
                    break
                if board[nx][ny] == 0 : # 빈 칸일 경우
                    data = []
                    break
                if board[nx][ny] == t : # 같은 돌일 경우
                    break
                else :
                    data.append((nx, ny))
                nx, ny = nx + dx, ny + dy

            for tx, ty in data :
                # 같은 돌로 갱신
                if t == 1 :
                    board[tx][ty] = 1
                elif t == 2 :
                    board[tx][ty] = 2
        board[x][y] = t

    W_cnt, B_cnt = 0, 0
    for i in range(n) :
        W_cnt += board[i].count(2)
        B_cnt += board[i].count(1)

    print('#%d %d %d' % (tc, B_cnt, W_cnt))
    
'''
1. 8개의 방향을 담은 direction 리스트를 정의한다.

2. 각 테스트 케이스마다 입력받은 n을 통해 n x n 크기의 board 리스트를 정의한다.

3. 바둑판 크기의 중간 값을 구하여 mid에 할당하고, 처음 board 상태를 정의한다.

4. m개의 입력값을 받고, 각 상황마다 인접한 8칸을 확인하여 아래와 같이 작업한다.
  - 만약 인접한 칸(board[nx][ny])이 범위를 벗어난다면 data 리스트를 초기화해준 뒤 break 한다.
  - 만약 board[nx][ny] 값이 0(빈 칸)일 경우 data 리스트를 초기화해준 뒤 break 한다.
  - 만약 board[nx][ny] 값이 현재의 돌과 같을 경우 break 한다.
  - 현재의 돌과 다를 경우 data 리스트에 해당 좌표(nx, ny)를 삽입한다.
  - 다음 인접한 칸을 확인하기 위해 nx, ny를 각각 다음 좌표로 갱신한다.

5. while문이 종료되면 data 리스트에 담겨 있는 좌표를 하나씩 꺼내고, 해당 좌표의 값을 현재의 돌과 같은 타입으로 갱신한다.

6. 8개의 방향을 모두 확인하면 원래의 좌표(x, y)의 값에 현재의 돌 타입을 삽입한다.

7. 최종적으로 board 리스트에 존재하는 흑돌의 개수, 백돌의 개수를 각각 구해 해당 테스트 케이스 번호와 함께 출력한다.

'''
