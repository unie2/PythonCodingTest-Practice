data = [list(map(int, input().split())) for _ in range(9)]

empty_list = []
for i in range(9) :
    for j in range(9) :
        if data[i][j] == 0 :
            empty_list.append((i, j))

def dfs(index) :
    if index == len(empty_list) :
        for i in range(9) :
            for j in range(9) :
                print(data[i][j], end=' ')
            print()
        exit(0)

    for i in range(1, 10) :
        x = empty_list[index][0]
        y = empty_list[index][1]

        if check_row(x, i) and check_col(y, i) and check_part(x, y, i) :
            data[x][y] = i
            dfs(index + 1)
            data[x][y] = 0

def check_row(x, num) :
    for i in range(9) :
        if data[x][i] == num :
            return False

    return True

def check_col(y, num) :
    for i in range(9) :
        if data[i][y] == num :
            return False

    return True

def check_part(x, y, num) :
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3) :
        for j in range(3) :
            if data[nx+i][ny+j] == num :
                return False

    return True

dfs(0)

'''
1. 9 x 9 크기의 격자판에서 0으로 입력된 좌표들을 empty_list에 할당하고, dfs() 함수를 호출한다.

2. dfs() 함수의 작업은 아래와 같다.
  - 만약 0으로 입력된 좌표의 개수(empty_list의 개수)와 index 값이 같다면 모든 좌표에 대한 갱신이 이루어졌으므로 격자판 상태를 출력하고 시스템을 종료한다.
  - 그렇지 않을 경우 empty_list의 index 번째 값(좌표)을 가져와 해당 위치를 기준으로 행, 열, 3 x 3 크기의 격자판 상태를 확인한다.
  - 이때 특정 숫자를 삽입하는 것에 대하여 세 가지의 방식에서 모두 True를 반환받았다면 해당 위치에 숫자를 삽입하고 dfs() 함수를 재귀호출한 뒤 해당 위치를 다시 0으로 갱신한다.

3. 특정 위치를 기준으로 3 x 3 크기의 격자판 상태를 확인하는 check_part() 함수의 작업은 아래와 같다.
  - 3 x 3 크기의 격자판 상태를 확인하는 가장 초기 값을 구해 각 nx, ny에 할당한다.
  - 각 위치의 값을 확인하여 그 값이 num과 같다면 숫자 num을 놓을 수 없으므로 False를 반환하고, 그렇지 않을 경우 True를 반환한다.

'''
