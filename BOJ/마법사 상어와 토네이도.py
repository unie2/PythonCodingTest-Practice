n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
x, y = n // 2, n // 2
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

windx = [
    # left
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    # down
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    # right
    [1, -1, 2, -2, 0, 1, -1, 1, -1],
    # up
    [1, 1, 0, 0, -2, 0, 0, -1, -1]
]
windy = [
    # left
    [1, 1, 0, 0, -2, 0, 0, -1, -1],
    # down
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    # right
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    # up
    [1, -1, 2, -2, 0, 1, -1, 1, -1]
]

rate = [1, 1, 2, 2, 5, 7, 7, 10, 10]

def wind(x, y, dir) :
    value = 0
    sand = data[x][y]
    sum_value = 0
    for i in range(9) :
        nx = x + windx[dir][i]
        ny = y + windy[dir][i]
        wind_sand = (sand * rate[i]) // 100
        sum_value += wind_sand

        if not (0 <= nx < n and 0 <= ny < n) :
            value += wind_sand
            continue
        data[nx][ny] += wind_sand

    nx = x + dx[dir]
    ny = y + dy[dir]
    a = sand - sum_value
    if not (0 <= nx < n and 0 <= ny < n) :
        value += a
    else :
        data[nx][ny] += a

    data[x][y] = 0
    return value

def solve(x, y) :
    value = 0
    visited = [[False] * n for _ in range(n)]
    dir = -1
    while True :
        if x == 0 and y == 0 :
            break
        visited[x][y] = True
        nd = (dir + 1) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]

        if visited[nx][ny] :
            nd = dir
            nx = x + dx[nd]
            ny = y + dy[nd]
        value += wind(nx, ny, nd)
        x, y, dir = nx, ny, nd

    return value


result = solve(x, y)

print(result)


'''
1. 초기 위치(x, y)는 중앙에서 시작하므로 입력받은 n을 2로 나눈 값을 x와 y에 할당한다.

2. 토네이도는 왼쪽, 아래, 오른쪽, 위 순서로 수행되기 때문에 해당 순서대로 좌표를 구성하여 dx, dy를 정의한다.

3. 아래 그림()을 참고하여 비율이 작은 순서대로 인덱스를 설정하여 'y'가 해당 좌표로 갈 수 있는 좌표 windx, windy를 정의한다.
   또한, 9개의 비율 값을 순서대로 rate 리스트에 담는다.
   
4. 현재의 좌표 x, y를 매개변수로 하여 solve() 함수를 호출하고 반환받은 값을 result에 할당한다.
   solve() 함수의 작업은 아래와 같다.
  - x, y가 (0, 0)이 될 때까지 반복 수행하며, 현재의 좌표를 방문처리(visited) 해주고 다음 방향과 방향을 바탕으로 다음 좌표를 구한다.
  - 만약 다음 좌표가 이미 방문처리가 되어 있다면 방향과 좌표를 이전으로 되돌린다.
  - 이후, 다음 좌표와 방향을 매개변수로 하여 wind() 함수를 호출하고 반환받은 값을 value에 누적한다.
  - 다음 반복 작업을 위해 현재의 좌표와 방향을 다음 좌표와 방향으로 갱신해준다.
  - 좌표가 (0, 0) 이 되었을 때 반복 작업을 끝내고 value 값을 반환한다.

5. wind() 함수의 작업은 아래와 같다.
  - 9개의 비율 값들을 하나씩 확인하는데, 해당 비율 값으로 가는 좌표 nx, ny를 정의한다.
  - 정의된 좌표에 어느정도의 모래가 가야하는지를 구하기 위해 현재의 모래(sand)에 비율을 곱하여 100으로 나눈 값을 wind_sand에 할당하고, sum_value 값에 누적한다.
  - 만약 해당 좌표가 범위를 벗어났다면 value에 wind_sand 값을 누적하고 continue를 수행한다.
  - 범위를 벗어나지 않았다면 wind_sand의 값을 다음 좌표(nx, ny)에 더해준다.
  - 9번의 작업을 다 수행하였다면, 알파(a)에 위치(nx, ny)하는 모래의 양을 구하기 위해 sand에서 옮긴 모래의 총합(sum_value)을 빼준다.
  - 알파의 위치가 범위를 벗어난다면 value에 알파 값(a)을 더해주고, 범위 내에 있다면 이동이 가능하므로 data[nx][ny] 값에 a를 더해준다.
  - 이후 현재 좌표(x, y)의 값을 0으로 갱신한 후 value 값을 반환한다.

6. 최종적으로 반환받은 값(result)을 출력한다.

'''
