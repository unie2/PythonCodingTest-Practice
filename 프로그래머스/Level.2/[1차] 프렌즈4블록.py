def solution(m, n, board) :
    answer = 0
    board = list(list(b) for b in board)

    while True :
        delete = []
        flag = False
        # 제거할 위치 찾기
        for i in range(m-1) :
            for j in range(n-1) :
                if board[i][j] != 0 and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] :
                    delete.append((i, j))
                    delete.append((i, j+1))
                    delete.append((i+1, j))
                    delete.append((i+1, j+1))
                    flag = True

        if flag == False :
            break

        # 위치 제거
        for x, y in delete :
            board[x][y] = 0

        # 남쪽 방향으로 위치 이동
        for i in range(m-1, -1, -1) :
            for j in range(n) :
                if board[i][j] == 0 :
                    x = i - 1
                    while x >= 0 and board[x][j] == 0 :
                        x -= 1
                    if x < 0 :
                        board[i][j] = 0
                    else :
                        board[i][j] = board[x][j]
                        board[x][j] = 0

    for i in range(m) :
        answer += board[i].count(0)

    return answer
  
'''
1. (0, 0) 좌표부터 (m-1, n-1) 좌표까지 각 칸의 값을 확인하며, 해당 칸을 포함하여 2 x 2 크기의 정사각형이 모두 같은 문자라면 delete리스트에 네 좌표 값을 할당하고 flag 값을 True로 갱신한다.
2. 만약 flag 값이 False라면 제거해야할 좌표가 없으므로 while문을 빠져나온다.
3. 제거해야할 좌표가 있다면 delete리스트에서 좌표(x, y)를 하나씩 꺼내 board[x][y]의 값을 0으로 갱신한다.
4. 이후 남쪽 방향으로 값들을 땡겨준다.
5. while문이 종료되면 board 리스트에서 0의 개수를 세어 answer에 누적하고, 최종적으로 answer 값을 반환한다.

'''
