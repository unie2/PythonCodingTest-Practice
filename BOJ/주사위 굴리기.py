n, m, x, y, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
ball = [0] * 6
directions = list(map(int, input().split()))

dx = [0, 0, -1, 1] # 동 서 북 남
dy = [1, -1, 0, 0]

for i in range(k) :
    direction = directions[i] - 1
    nx = x + dx[direction]
    ny = y + dy[direction]
    if not 0 <= nx < n or not 0 <= ny < m :
        continue

    if direction == 0 : # 동쪽일 경우
        # 상단, 오른쪽, 왼쪽, 바닥
        ball[0], ball[2], ball[3], ball[5] = ball[3], ball[0], ball[5], ball[2]
    elif direction == 1 : # 서쪽일 경우
        # 상단, 오른쪽, 왼쪽, 바닥
        ball[0], ball[2], ball[3], ball[5] = ball[2], ball[5], ball[0], ball[3]
    elif direction == 2 : # 북쪽일 경우
        # 상단, 정면, 후면, 바닥
        ball[0], ball[1], ball[4], ball[5] = ball[4], ball[0], ball[5], ball[1]
    else : # 남쪽일 경우
        # 상단, 정면, 후면, 바닥
        ball[0], ball[1], ball[4], ball[5] = ball[1], ball[5], ball[0], ball[4]

    if data[nx][ny] == 0 : # 칸에 쓰여있는 수가 0일 경우
        # 주사위의 바닥면에 쓰여있는 수가 칸에 복사
        data[nx][ny] = ball[5]
    else : # 0이 아닐 경우
        # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0으로 갱신
        ball[5] = data[nx][ny]
        data[nx][ny] = 0
    # 다음 작업을 위해 현재의 좌표를 x, y에 갱신
    x, y = nx, ny
    # 주사위 상단에 쓰여 있는 값 출력
    print(ball[0])
    
'''
1. 동 서 북 남 순서로 좌표 dx, dy를 정의한다.
2. 반복문 내에서는 입력받은 이동하는 명령을 의미하는 directions의 요소를 하나씩 확인하여 인덱스를 맞춰주기 위해 1 감소시킨 인덱스의 값으로 꺼낸다.
3. 꺼낸 이동 정보(direction)를 바탕으로 이동시킬 좌표를 구하여 nx, ny에 할당한다.
4. 해당 좌표가 지도 범위를 넘어간다면 continue를 통해 이후 작업을 하지 않고 넘어간다.
5. 지도 범위 내에 있다면 이동값을 기준으로 주사위를 굴린다.
6. 이후 칸에 쓰여 있는 수가 0일 경우 주사위의 바닥면에 쓰여 있는 수가 칸에 복사되도록 하고, 0이 아닐 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되고 칸에 쓰여 있는 수는 0으로 갱신한다.
7. 다음 요소의 작업을 위해 현재의 좌표(nx, ny)를 x, y에 갱신하고, 주사위 상단에 쓰여 있는 값(ball[0])을 출력한다.


'''
