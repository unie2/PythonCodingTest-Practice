t = int(input())
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(1, t + 1) :
    n = int(input())
    data = [[0] * n for _ in range(n)]
    # 초기 위치 및 회전 방향 정의
    x, y = 0, 0
    direction = 0

    for j in range(1, n * n + 1) :
        data[x][y] = j
        x += dx[direction]
        y += dy[direction]

        if not 0 <= x < n or not 0 <= y < n or data[x][y] != 0 :
            x -= dx[direction]
            y -= dy[direction]
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]

    print('#%d' % i)
    for j in range(n) :
        for k in range(n) :
            print(data[j][k], end=' ')
        print()
        
        
'''
1. 문제에서 요구하는 바와 같이 2차원 리스트에 알맞는 수를 부여하기 위해 우, 하, 좌, 상 방향의 dx, dy를 정의한다.
2. 각 테스트 케이스마다 n을 입력받아 n x n 크기의 2차원 리스트 data를 정의한다.
3. 초기 위치(x, y) 및 회전 방향(direction)을 0으로 초기화한다.
4. 반복문을 통해 해당 좌표에 수를 부여하고, 다음 좌표를 구하여 해당 좌표가 리스트 범위 안에 없거나 이미 값이 부여된 경우 아래와 같이 작업한다.
  - 다음 좌표를 이전으로 되돌리고, 다음 방향을 구해 구한 방향을 바탕으로 다음 좌표를 구한다.
5. 이와 같은 반복 작업이 끝나면 최종적으로 해당 테스트 케이스 번호와 함께 data 리스트 값들을 출력한다.

'''
