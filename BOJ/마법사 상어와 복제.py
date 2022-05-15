# ←, ↖, ↑, ↗, →, ↘, ↓, ↙ (45도 반시계 주의! - 물고기 이동)
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# 상어 (상좌하우) 연속해서 3칸 이동
shark_dx = [-1, 0, 1, 0]
shark_dy = [0, -1, 0, 1]

m, s = map(int, input().split()) # 물고기의 수, 연습 횟수
fish = [[[[], []] for _ in range(4)] for _ in range(4)]
fish_smell = [[0] * 4 for _ in range(4)]

for _ in range(m) :
    x, y, d = map(int, input().split()) # 물고기의 위치, 방향
    fish[x-1][y-1][0].append(d-1) # 해당 좌표에 방향 삽입

x, y = map(int, input().split()) # 상어의 위치
x -= 1
y -= 1 # 인덱스로 인해 위치 재설정
path = []
max_fish_count = -1

visited = [[False] * 4 for _ in range(4)]

# 1. 복제 마법 시전 (물고기 복제) 함수
def copy_start() :
    for i in range(4) :
        for j in range(4) :
            for dir in fish[i][j][0] :
                fish[i][j][1].append(dir)

# 2. 물고기 이동 함수
def move_fish() :
    position = []
    for i in range(4) :
        for j in range(4) :
            while fish[i][j][0] :
                nd = fish[i][j][0].pop()
                flag = False
                for _ in range(8) : # 8칸에 대하여 확인
                    nx = i + dx[nd]
                    ny = j + dy[nd]
                    # 이동할 수 있는 경우
                    if 0 <= nx < 4 and 0 <= ny < 4 and fish_smell[nx][ny] == 0 and not (nx == x and ny == y) :
                        position.append((nx, ny, nd))
                        flag = True
                        break
                    # 이동할 수 없는 경우
                    nd = (nd - 1) % 8
                if flag == False :
                    position.append((i, j, nd)) # 모두 이동할 수 없다면 이동 안함
    return position

def select_move_shark(r, c, fish_count, move_count, temp_path) :
    global x, y, visited, max_fish_count, path
    if move_count == 3 : # 3번 이동했다면
        if max_fish_count < fish_count :
            max_fish_count = fish_count
            path = [d for d in temp_path]
        return

    for d in range(4) : # 네 가지 방향에 대해서
        nx = r + shark_dx[d]
        ny = c + shark_dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4 : # 범위를 벗어나지 않는다면
            if not visited[nx][ny] : # 방문한 적이 없다면
                visited[nx][ny] = True # 방문처리
                next_fish_count = fish_count + len(fish[nx][ny][0])
                select_move_shark(nx, ny, next_fish_count, move_count+1, temp_path+[d])
                visited[nx][ny] = False
            else :
                select_move_shark(nx, ny, fish_count, move_count+1, temp_path+[d])

def move_shark() :
    global x, y, fish, fish_smell
    for d in path :
        x = x + shark_dx[d]
        y = y + shark_dy[d]
        if fish[x][y][0] :
            fish[x][y][0] = []
            fish_smell[x][y] = 3 # 2가 아닌 3인 이유는 바로 다음 단계에서 1을 감소시키기 떄문

def reduce_smell() :
    global fish_smell
    for i in range(4) :
        for j in range(4) :
            if fish_smell[i][j] > 0 :
                fish_smell[i][j] -= 1

def copy_end() :
    global fish
    for i in range(4) :
        for j in range(4) :
            while fish[i][j][1] :
                fish[i][j][0].append(fish[i][j][1].pop())

for now in range(s) :
    # 1. 복제 마법 시전 (물고기 복제)
    copy_start()
    # 2. 물고기 이동
    position = move_fish()
    for r, c, dir in position :
        fish[r][c][0].append(dir)

    path = []
    max_fish_count = -1

    # 3. 상어 이동
    select_move_shark(x, y, 0, 0, [])
    move_shark()

    # 4. 냄새 감소
    reduce_smell()
    # 5. 복제 완료
    copy_end()

result = 0
for i in range(4) :
    for j in range(4) :
        result += len(fish[i][j][0])

print(result)


'''
1. 문제에서 제시한 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 방향 순서로 dx, dy를 정의한다.

2. '노트'에서 (상 좌 하 우) 순으로 수가 커지기 때문에 해당 순서로 상어가 이동하는 방향 shark_dx, shark_dy를 정의한다.

3. 각 물고기의 방향을 담는 fish 리스트를 정의한다. 여기서 첫번째 요소는 현재의 위치에 대한 방향이며, 두번째 요소는 복제를 위해 정의하였다.

4. 각 칸에 대해 물고기의 냄새를 남기기 위한 fish_smell 리스트를 정의한다.

5. m개의 물고기 정보를 입력받아 fish 리스트 내 해당 좌표에 방향을 삽입한다.

6. 입력받은 s번만큼 반복 수행하며, 하나의 작업에서는 다음과 같이 수행한다.
  - (1: 복제 마법 시전) copy_start() 함수를 통해 복제 마법을 시전한다. fish리스트의 해당 위치에 존재하는 두번째 요소에 방향을 삽입한다.
  - (2: 물고기 이동) move_fish() 함수를 통해 이동시킬 물고기의 좌표와 방향을 가져와 이동시킨다.
  - (3: 상어 이동) select_move_shark() 함수를 통해 상어가 이동할 방향을 구하고 move_shark() 함수를 통해 상어를 이동시킨다.
  - (4: 냄새 감소) reduce_smell() 함수를 통해 물고기의 냄새가 있는 칸의 냄새를 1 감소시킨다.
  - (5: 복제 완료) fish 리스트의 두번째 요소를 첫번째 요소로 옮김으로써 복제를 완료한다.
  - s번의 작업이 끝나면 최종적으로 격자에 있는 물고기의 수를 result 값에 누적하여 출력한다.

7. 물고기가 이동할 수 있는 좌표와 방향을 구하는 move_fish() 함수의 작업은 아래와 같다.
  - 각 칸에 물고기가 있다면 해당 물고기의 방향을 nd에 할당하고 flag를 False로 초기화해준다.
  - 8칸에 대하여 이동할 수 있는지 확인하는데, 이동할 칸이 범위를 벗어나거나 물고기의 냄새가 존재하거나 상어가 있는 좌표라면 다음 방향을 확인한다. 
    (여기서 주의할 점은 (nd - 1) % 8 이다. 45도 반시계 방향으로 확인해야 하므로 nd + 1이 아닌 nd - 1로 해야한다.)
  - 만약 위 조건에 해당되지 않고 이동할 수 있다면 position 리스트에 이동할 칸의 좌표와 방향을 삽입하고 flag 값을 True 갱신한 후 break한다.
  - flag 값이 False라면 position 리스트에 현재의 좌표와 방향을 할당하고, 모든 칸에 대하여 확인을 마쳤다면 position 리스트를 반환한다.

8. 상어가 이동할 방향을 구하는 select_move_shark() 함수의 작업은 아래와 같다.
  - 네 가지 방향에 대하여 이동시킬 위치를 구하고 이동할 칸이 범위를 벗어나지 않고 방문한 적이 없다면 방문처리를 해주고 물고기 수를 누적하여 함수를 재귀 호출한다.
    함수 호출 이후에는 방문 처리를 다시 해제하여 다른 경우에서도 확인할 수 있도록 한다.
  - 방문한 적이 있다면 물고기를 중복으로 세면 안되므로 fish_count 값 그대로를 매개변수로 하여 재귀 호출한다.
  - move_count 값이 3일 경우 상어가 3번 이동했음을 의미하므로 max_fish_count를 갱신해주고 방향을 path에 저장한 후 return 한다.

9. 상어가 이동할 방향이 담긴 path를 활용하여 상어를 이동시킬 move_shark() 함수의 작업은 아래와 같다.
  - path리스트에서 방향을 하나씩 꺼내 해당 위치에 물고기가 존재하면 물고기를 제거하고 냄새를 3으로 설정하여 남긴다. 
    여기서 냄새를 2가 아닌 3으로 설정한 이유는 바로 다음 단계에서 1을 감소시키기 때문이다.

'''
