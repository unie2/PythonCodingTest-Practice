t = int(input())

def matrix(x, y) :
    i, j = x, y
    row = 1
    column = 1

    while True :
        x += 1
        if x < n and data[x][y] != 0 and visited[x][y] == False :
            row += 1
        else :
            x -= 1
            break
    while True :
        y += 1
        if y < n and data[x][y] != 0 and visited[x][y] == False :
            column += 1
        else :
            y -= 1
            break

    for k in range(i, x + 1) :
        for l in range(j, y + 1) :
            visited[k][l] = True

    return [row, column]

for tc in range(1, t + 1) :
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    result = []

    for i in range(n) :
        for j in range(n) :
            if data[i][j] != 0 and visited[i][j] == False :
                value = matrix(i, j)
                result.append(value)

    result = sorted(result, key=lambda x: (x[0] * x[1], x[0]))
    print('#%d %d' % (tc, len(result)), end=' ')
    for r in result :
        print(*r, end=' ')
    print()
    
    
'''
1. 각 테스트 케이스마다 방문 여부를 확인하기 위한 n x n 크기의 visited 2차원 리스트를 정의한다.

2. n x n 크기의 data 2차원 리스트의 값을 하나씩 확인하며, 만약 그 값이 0이 아니고 방문하지 않았다면 해당 좌표를 matrix() 함수에 전달한 후 반환받은 값을 result에 추가한다.

3. result 리스트 요소를 정렬하는데, (각 행렬의 곱 -> 행) 순으로 정렬을 수행한다.

4. 최종적으로 해당 테스트 케이스 번호와 함께 부분 행렬들의 개수와 행과 열의 크기를 출력한다.

5. matrix() 함수의 작업은 아래와 같다.
  - i, j에 각 x, y를 담고, row 값과 column 값을 1로 초기화한다.
  - 전달받은 좌표를 기준으로 하여 while문을 통해 행 길이를 구하고, 열 길이를 구한다.
  - 2중 for문을 통해 부분 행렬 범위 내 visited 값을 True로 갱신한다.
  - [row, column] 형태의 값을 반환한다.

'''
