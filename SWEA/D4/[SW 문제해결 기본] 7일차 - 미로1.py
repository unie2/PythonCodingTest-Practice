dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y) :
    global data, visited
    if (x, y) == (13, 13) :
        return True
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < 16 and 0 <= ny < 16) :
            continue
        if data[nx][ny] == '0' or data[nx][ny] == '3' :
            if visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                if check(nx, ny) :
                    return True
                visited[nx][ny] = 0

for _ in range(10) :
    tc = int(input())
    data = [list(input()) for _ in range(16)]
    x, y = 1, 1
    visited = [[0] * 16 for _ in range(16)]
    visited[x][y] = 1

    if check(x, y) :
        print('#%d %d' % (tc, 1))
    else :
        print('#%d %d' % (tc, 0))
        
'''
1. 특정 위치에서 (상, 하, 좌, 우) 방향에 인접한 칸을 확인하기 위해 dx, dy 리스트를 정의한다.

2. 각 테스트 케이스마다 미로판 상태(data)를 입력받고 시작점(x, y)을 (1, 1)로 설정한다.
   또한, 방문 여부를 확인하기 위한 visited 리스트를 정의하고, 시작점의 visited 값을 1로 갱신하여 방문 처리한다.

3. check() 함수에 x, y를 전달하여 반환받은 값이 True일 경우 해당 테스트 케이스 번호와 함께 1을 출력하고, 그렇지 않다면 0을 출력한다.

4. check() 함수의 작업은 아래와 같다.
  - 전달받은 x, y의 값이 모두 13일 경우 True를 반환한다.
  - 네 방향의 인접한 값을 각각 확인하는데, 범위를 벗어난다면 continue를 수행하고, 범위 내에 있다면 해당 위치의 값을 확인한다.
  - 만약 그 값이 '0' 이거나 '3'이고 방문처리 되어 있지 않는다면 방문처리를 수행하고 check() 함수에 해당 좌표(nx, ny)를 매개변수로 하여 재귀호출한다.
  - 재귀 호출을 수행한 후에는 방문 처리를 다시 해제해준다.

'''
