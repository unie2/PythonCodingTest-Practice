t = int(input())

direction = [(-2, 0), (2, 0), (0, -2), (0, 2), (-1, -1), (1, -1), (1, 1), (-1, 1)]
for tc in range(1, t + 1) :
    data = list(str(input()))
    board = [['.' for _ in range(len(data) * 4 + 1)] for _ in range(5)]
    index = 5 // 2
    for i in range(2, len(board[0]), 4) :
        board[index][i] = data.pop(0)
        for d in range(8) :
            nx, ny = direction[d]
            nx = index + nx
            ny = i + ny
            board[nx][ny] = '#'

    for i in range(len(board)) :
        print(''.join(board[i]))
        
'''
1. 두 칸 이후에 '#' 문자를 넣을 (상 하 좌 우) 방향과 한 칸 이후 '#' 문자를 넣을 대각선 네 방향을 direction 리스트에 저장한다.
2. 각 테스트 케이스마다 data를 입력받아 중간 위치에 4칸 단위로 data 문자열의 문자를 하나씩 넣는다.
3. 문자를 하나씩 넣을 때마다 해당 위치를 기준으로 하여 8개의 방향(direction)에 '#' 문자를 할당한다.
4. 최종적으로 board 상태를 문제에서 요구한 출력 형식에 맞추어 출력한다.

'''
