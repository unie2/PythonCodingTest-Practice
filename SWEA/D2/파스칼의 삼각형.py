t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    board = [[0] * n for _ in range(n)]
    for i in range(n) :
        board[i][0] = 1

    for i in range(1, n) :
        for j in range(1, n) :
            board[i][j] = board[i-1][j-1] + board[i-1][j]

    print('#%d' % tc)
    for i in range(n) :
        for j in range(n) :
            if board[i][j] != 0 :
                print(board[i][j], end=' ')
        print()
        
'''
1. 각 테스트 케이스마다 N x N 크기의 board 리스트를 정의하고 모든 행의 0번째 요소를 1로 갱신한다.
2. board 리스트의 1번째 행, 1번째 열부터 해당 인덱스의 값을 왼쪽 대각선 위(board[i-1][j-1])와 위(board[i-1][j])에 존재하는 값의 합으로 갱신한다.
3. board 리스트의 요소를 하나씩 출력하는데 해당 위치의 값이 0이 아닐 경우에만 값을 출력하고 한 행에 대한 작업이 끝나면 줄바꿈을 수행한다.

'''
