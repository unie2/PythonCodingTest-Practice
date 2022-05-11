n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chess = [[[] for _ in range(n)] for _ in range(n)]
# 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
horse = []

for i in range(k) :
    r, c, d = map(int, input().split())
    horse.append([r-1, c-1, d-1])
    chess[r-1][c-1].append(i)

result_turn = 0

def solve(horse_num) :
    x, y, dir = horse[horse_num]
    nx = x + dx[dir]
    ny = y + dy[dir]
    if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2 :
        if dir in [0, 2] :
            dir += 1
        elif dir in [1, 3] :
            dir -= 1
        horse[horse_num][2] = dir
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2 :
            return True

    horse_add = []
    for idx, number in enumerate(chess[x][y]) :
        if number == horse_num :
            horse_add.extend(chess[x][y][idx:])
            chess[x][y] = chess[x][y][:idx]
            break

    if board[nx][ny] == 1 : # 빨간색
        horse_add = horse_add[-1::-1] # 말을 거꾸로

    for h in horse_add :
        horse[h][0], horse[h][1] = nx, ny # 말 이동
        chess[nx][ny].append(h) # 말 쌓아 올리기

    if len(chess[nx][ny]) >= 4 :
        return False
    return True

while True :
    flag = False
    if result_turn > 1000 :
        print(-1)
        break

    for l in range(k) :
        if solve(l) == False :
            flag = True
            break

    result_turn += 1
    if flag == True :
        print(result_turn)
        break
        
'''
1. 체스판의 정보를 입력받아 board 리스트를 정의하고, 특정 위치에 말의 번호를 담을 chess 리스트와 말의 좌표와 방향을 담을 horse 리스트를 정의한다.

2. (동 서 북 남) 순서로 방향을 구성하는 dx, dy 리스트를 정의한다.

3. k개의 말의 정보를 입력받아 각 말의 정보를 horse 리스트에 추가하고, chess 리스트의 해당 말의 좌표에 말의 번호를 추가한다.

4. 반복문을 통해 작업을 수행하며, 수행 작업은 아래와 같다.
  - 턴의 번호(result_turn)가 1000보다 커지면 -1을 출력하고 작업을 종료한다.
  - 1000보다 작거나 같을 경우 반복문을 통해 말의 번호가 작은 순서로 solve() 함수를 수행한다.
  - solve() 함수를 통해 받은 값이 False 일 경우 flag 값을 True로 갱신하고 break 한다.
  - 턴의 번호(result_turn)를 1 증가시킨 후 만약 flag 값이 True 라면 result_turn을 출력하고 작업을 끝낸다.

5. solve() 함수의 작업은 아래와 같다.
  - 전달받은 horse_num을 인덱스로 하여 horse 리스트에서 해당 말의 좌표와 방향을 x, y, dir 에 할당한다.
  - 정의된 방향(dir)을 통해 말을 이동시킬 다음 좌표를 구하여 nx, ny에 할당한다.
  - 만약 다음 좌표가 체스판의 범위를 벗어나거나 다음 좌표의 칸이 파란색(2)일 경우 방향을 반대로 바꾸고 바꾼 방향에 대해 이동시킬 다음 좌표를 구하여 nx, ny를 갱신한다.
  - 다시 다음 좌표에 대한 상황을 확인하여 이 또한 범위를 벗어나거나 파란색일 경우 True를 반환한다.

  - 다음 좌표로 이동 시킬 말의 번호를 담을 horse_add 리스트를 정의한다.
  - enumerate() 를 통해 인덱스와 말의 번호(number)를 가져와 number와 horse_num이 같을 경우 해당 말의 번호와 그 위에 쌓여있는 말의 번호들을 순서대로 horse_add 리스트에 추가한다.
  - 또한, horse_add 에 추가된 말들을 제외하여 chess 리스트를 갱신하고 break 한다.
 
  - 만약 이동하려는 칸이 빨간색(1)일 경우 horse_add 리스트를 거꾸로 뒤집어 준다.
  - 반복문을 통해 horse_add 리스트에 담겨 있는 각 말들의 좌표를 다음 좌표(nx, ny)로 갱신해주고 말들을 이동시킨다.
  - 만약 이동한 좌표에 존재하는 말들이 4개 이상일 경우 False를 반환한다.

'''
