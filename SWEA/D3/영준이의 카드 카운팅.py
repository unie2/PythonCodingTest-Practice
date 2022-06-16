t = int(input())

for tc in range(1, t + 1) :
    board = [13] * 4 # S, D, H, C 순
    data = input()

    visited = []

    for i in range(0, len(data), 3) :
        if data[i] == 'S' :
            board[0] -= 1
        elif data[i] == 'D' :
            board[1] -= 1
        elif data[i] == 'H' :
            board[2] -= 1
        else :
            board[3] -= 1
        if data[i:i+3] in visited :
            board = 'ERROR'
            break
        visited.append(data[i:i+3])

    if board == 'ERROR' :
        print('#%d %s' % (tc, board))
    else :
        print(f'#{tc}', *board)
        
'''
1. 각 테스트 케이스마다 13으로 초기화된 4개의 값이 담긴 board 리스트를 정의하고, data를 입력받는다.

2. 입력받은 문자열에서 알파벳 문자를 확인하는데, 각 문자에 대한 board 값을 1 감소시킨다.

3. 이후 TXY 꼴의 문자열(ex. S01)이 visited 리스트에 존재한다면 board를 'ERROR' 문자열로 갱신하고 break 한다.

4. visited 리스트에 존재하지 않는다면 TXY 꼴의 문자열을 visited 리스트에 추가한다.

5. 반복문 작업이 끝나면 board 값을 확인하고, board가 'ERROR' 일 경우 해당 테스트 케이스 번호와 함께 문자열 형태로 board를 출력하고,
   그렇지 않다면 board 리스트 내에 존재하는 요소들을 출력한다.

'''
