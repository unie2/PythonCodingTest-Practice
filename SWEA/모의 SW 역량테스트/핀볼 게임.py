t = int(input())
# 위 오른쪽 아래 왼쪽
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 5개의 블록 방향 정의 (각 위로, 오른쪽으로, 아래로, 왼쪽으로 갈 때)
blocks = [
    [],
    [2, 3, 1, 0],
    [1, 3, 0, 2],
    [3, 2, 0, 1],
    [2, 0, 3, 1],
    [2, 3, 0, 1]
]

def check(x, y) :
    if 0 <= x < n and 0 <= y < n :
        return True
    return False

def get_score(start_x, start_y, start_dir) :
    score = 0
    dx, dy, dir = start_x, start_y, start_dir

    while True :
        dx = dx + directions[dir][0]
        dy = dy + directions[dir][1]
        if check(dx, dy) : # 범위 내에 존재한다면
            # 만약 블록을 만났을 경우
            if data[dx][dy] in range(1, 6) :
                block_type = data[dx][dy]
                # 점수 증가
                score += 1
                dir = blocks[block_type][dir]
                continue
            # 만약 웜홀을 만났을 경우
            elif data[dx][dy] in range(6, 11) :
                hall_type = data[dx][dy]
                if (dx, dy) == wormhole[hall_type][0] :
                    dx, dy = wormhole[hall_type][1]
                else :
                    dx, dy = wormhole[hall_type][0]
                continue
            # 만약 블랙홀을 만났을 경우
            elif data[dx][dy] == -1 :
                return score
            # 시작점으로 도달했을 경우
            elif (dx, dy) == (start_x, start_y) :
                return score
            # 빈 공간일 경우
            else :
                continue
        # 벽을 만났을 경우
        else :
            dir = (dir + 2) % 4 # 반대 방향으로 전환
            score += 1


for tc in range(1, t + 1) :
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    # 웜홀 리스트
    wormhole = [[] for _ in range(11)]
    for i in range(n) :
        for j in range(n) :
            value = data[i][j]
            if value in range(6, 11) : # 웜홀일 경우
                wormhole[value].append((i, j)) # 좌표 삽입

    for i in range(n) :
        for j in range(n) :
            if data[i][j] == 0 : # 빈 공간이면
                for k in range(4) : # 네 방향 확인
                    score = get_score(i, j, k)
                    result = max(result, score)

    print('#%d %d' % (tc, result))
    
'''
1. (위, 오른쪽, 아래, 왼쪽) 방향의 directions와 (위, 오른쪽, 아래, 왼쪽) 방향으로 각 블록을 맞닿았을 경우 전환해야 할 방향을 담는 blocks 리스트를 정의한다.

2. 각 테스트 케이스마다 N x N 크기의 data 리스트와 웜홀의 위치 좌표를 담을 wormhole 리스트를 정의한다.

3. data 리스트의 요소를 하나씩 확인하며, 그 값이 웜홀일 경우 웜홀 번호를 인덱스로하여 wormhole 리스트에 좌표를 추가한다.

4. 웜홀 좌표를 구하는 작업을 마치면 다시 data 리스트의 요소를 하나씩 확인하여 그 값이 빈 공간(0) 일 경우 아래와 같이 수행한다.
  - 인접한 네 방향(위, 오른쪽, 아래, 왼쪽)을 확인하며, get_score() 함수를 호출해 반환받은 점수를 result 값과 비교하여 최대값을 구해 result에 갱신한다.

5. get_score() 함수의 작업은 아래와 같다.
  - 전달받은 좌표(start_x, start_y, start_dir)를 dx, dy, dir에 각각 할당한다.
  - 반복문을 수행하며, 핀볼이 이동할 다음 좌표를 구한다. 다음 좌표가 범위 내에 존재할 경우 아래와 같이 수행한다.
  - 다음 좌표가 블록일 경우 블록의 종류(번호)를 구하고 점수를 1 증가시킨 후 dir 값을 블록이 이동해야할 방향으로 갱신한다. 이후 continue 작업을 통해 다음 좌표를 확인한다.
  - 만약 웜홀을 만났을 경우 웜홀의 종류(번호)를 구하고 다른 좌표에 있는 같은 종류의 웜홀의 좌표로 dx, dy를 갱신한다. 이후 continue 작업을 통해 다음 좌표를 확인한다.
  - 만약 블랙홀을 만났을 경우 혹은 시작점으로 도달했을 경우에는 점수(score)를 반환한다.
  - 만약 다음 좌표가 단순히 빈 공간일 경우 continue 작업을 통해 다음 좌표를 확인한다.

  - 만약 다음 좌표가 범위 내에 존재하지 않을 경우(벽을 만났을 경우) 반대 방향으로 전환하고 점수를 1 증가시킨다.

6. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
