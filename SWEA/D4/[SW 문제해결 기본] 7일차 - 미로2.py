dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y) :
    global visited
    q = []
    q.append((x, y))

    while q :
        rx, ry = q.pop(0)
        for i in range(4) :
            nx = rx + dx[i]
            ny = ry + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100 and data[nx][ny] in [0, 3] and (nx, ny) not in visited :
                q.append((nx, ny))
                visited.append((nx, ny))
                if data[nx][ny] == 3 :
                    return True


for _ in range(10) :
    tc = int(input())
    data = [list(map(int, input())) for _ in range(100)]
    x, y = 1, 1
    visited = []
    if check(x, y) :
        print('#%d %d' % (tc, 1))
    else :
        print('#%d %d' % (tc, 0))
        
'''
1. 특정 위치에서 (상, 하, 좌, 우) 방향에 인접한 칸을 확인하기 위해 dx, dy 리스트를 정의한다.

2. 각 테스트 케이스마다 100 x 100 크기의 미로판 상태(data)를 입력받고 시작점(x, y)을 (1, 1)로 설정한다.
   또한, 방문 여부를 확인하기 위한 visited 리스트를 정의한다.

3. check() 함수에 x, y를 전달하여 반환받은 값이 True일 경우 해당 테스트 케이스 번호와 함께 1을 출력하고, 그렇지 않다면 0을 출력한다.

4. check() 함수의 작업은 아래와 같다.
  - q 리스트를 정의하고, 전달받은 (x, y)를 q 리스트에 추가한다.
  - q가 빌 때까지 q에서 (x, y)를 꺼내 rx, ry에 할당하고, 각 인접한 칸(nx, ny)이 범위 내에 존재하고 해당 좌표의 값이 0이거나 3이고, 방문처리 되지 않았다면
    q에 (nx, ny)를 추가하고 visited 리스트에도 (nx, ny)를 추가해줌으로써 방문처리를 해준다.
  - 만약 data[nx][ny]가 3일 경우 True를 반환한다.

'''
