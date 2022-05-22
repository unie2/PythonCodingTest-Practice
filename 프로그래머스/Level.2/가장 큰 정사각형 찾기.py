import itertools

def solution(board) :
    for i in range(1, len(board)) :
        for j in range(1, len(board[0])) :
            if board[i][j] == 1 :
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1

    return max(itertools.chain(*board)) ** 2
  
'''
1. 이중 for문을 통해 (1, 1) 좌표부터 확인하여 해당 좌표가 1일 경우 (위, 왼쪽, 대각선 왼쪽 위) 의 값중 최솟값을 도출하고 1을 더하여 board[i][j]에 할당한다.
2. 반복 작업이 끝나면 최종적으로 itertools.chain() 을 통해 board 리스트를 연결하여 최대값을 구해 제곱한 값을 반환한다.

'''
