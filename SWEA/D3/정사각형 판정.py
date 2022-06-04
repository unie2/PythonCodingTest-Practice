t = int(input())

def check(board, cnt, n) :
    for i in range(n) :
        for j in range(n) :
            if board[i][j] == 1 :
                down = 0
                right = 0
                for k in range(i+1, n) :
                    if board[k][j] == 1 :
                        down +=1
                    else :
                        break

                for k in range(j+1, n) :
                    if board[i][k] == 1 :
                        right += 1
                    else :
                        break

                if down != right :
                    return 'no'

                for x in range(i, i+down + 1) :
                    for y in range(j, j+right + 1) :
                        if board[x][y] == 1 :
                            cnt -= 1
                        else :
                            return 'no'

                if cnt != 0 :
                    return 'no'
                return 'yes'

for tc in range(1, t + 1) :
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n) :
        data = list(map(str, input()))
        for j in range(n) :
            c = data[j]
            if c == '#' :
                board[i][j] = 1
                cnt += 1
            else :
                continue

    result = check(board, cnt, n)
    print('#%d %s' % (tc, result))
    
'''
1. 각 테스트 케이스마다 0으로 초기화시킨 2차원 배열 board를 정의한다.

2. 격자판 상태를 한 줄씩 입력받고 해당 문자열의 문자를 하나씩 확인하는데, 만약 해당 문자가 '#'일 경우 해당 좌표의 board 리스트 값을 1로 갱신하고 cnt를 1 증가시킨다.

3. check() 함수를 통해 정사각형 판정 문자열을 반환받아 해당 테스트 케이스 번호와 함께 출력한다.

4. check() 함수의 작업은 아래와 같다.
  - board 리스트의 요소를 하나씩 확인하는데, 해당 좌표의 값이 1일 경우 아래로 이동하는 경로에서 값이 1이 나오는 횟수를 구해 down에 저장한다.
  - 또한, 오른쪽으로 이동하는 경로에서 값이 1이 나오는 횟수를 구해 right에 저장한다.
  - 만약 down과 right 값이 다르다면 정사각형을 이룰 수 없으므로 'no'를 반환한다.
  - 'no'가 반환되지 않았다면, 오른쪽 변에서 아래로 이동하는 경로를 확인하면서 cnt를 1씩 감소시키고, 반복문이 끝나지 않았음에도 해당 좌표가 1이 아닐 경우 'no'를 반환한다.
  - 만약 cnt 값이 0이 아닐 경우 'no'를 반환한다.
  - 위 작업을 마쳤음에도 'no'가 반환되지 않았다면 'yes'를 반환한다.

'''
