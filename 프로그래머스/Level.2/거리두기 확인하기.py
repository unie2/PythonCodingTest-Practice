dx = [-1, 1, 0, 0] # 인접한 네 칸에 대한 방향 (상 하 좌 우)
dy = [0, 0, -1, 1]
dx_2 = [-1, -1, 1, 1] # 대각선 방향
dy_2 = [-1, 1, -1, 1]

def check(board) :
    for i in range(5) :
        for j in range(5) :
            if board[i][j] == 'P' :
                # 인접한 네 방향 확인
                for d in range(4) :
                    r, c = i, j
                    for l in range(2) :
                        nx = r + dx[d]
                        ny = c + dy[d]
                        if not (0 <= nx < 5 and 0 <= ny < 5) :
                            continue
                        if board[nx][ny] == 'X' :
                            break
                        if board[nx][ny] == 'P' :
                            return False
                        r, c = nx, ny
                # 대각선 방향 확인
                for d in range(4) :
                    nx = i + dx_2[d]
                    ny = j + dy_2[d]
                    if not (0 <= nx < 5 and 0 <= ny < 5) :
                        continue
                    if board[nx][ny] == 'P' :
                        if board[nx][j] == 'X' and board[i][ny] == 'X' :
                            continue
                        else :
                            return False
    return True

def solution(places):
    result = []
    for i in range(len(places)) :
        arr = places[i]
        if check(arr) :
            result.append(1)
        else :
            result.append(0)
            
    return result
  
'''
1. 인접한 네 칸에 대한 확인과 대각선 칸에 대한 확인을 나누어서 문제를 해결하였다.

2. 전달받은 places에서 각 대기실 값을 빼내어 arr에 담고 check() 함수에 전달하여 받은 값이 True라면 result에 1을 추가하고, False라면 0을 추가한다.

3. check() 함수의 작업은 아래와 같다.
  - 전달받은 대기실 값에서 한 칸씩 확인하고, 해당 칸이 'P'일 경우 인접한 네 방향을 확인한다.
  - 한 방향에 대하여 맨해튼 거리를 2까지 확인하기 위해 반복문을 삽입하여 두 칸씩 확인할 수 있도록 한다.
  - 확인하는 칸이 범위를 벗어나면 continue를 진행하고, 'X' 라면 파티션이 막혀있으므로 break한다.
  - 만약 확인하는 칸이 'P'일 경우 거리두기를 지키지 않은 것이므로 False를 반환한다.
 
  - 인접한 네 방향에 대한 확인이 끝났음에도 False가 반환되지 않았다면 대각선 방향을 확인한다.
  - 대각선 방향은 각 방향에 대해서 한 칸씩만 확인해도 맨해튼 거리가 2이므로 이후 칸들을 확인할 필요가 없다.
  - 확인하고자 하는 칸이 범위를 벗어나면 continue를 진행한다.
  - 확인하고자 하는 칸이 'P'라면 현재 기준이 되는 칸과 확인하는 칸 사이를 확인하고, 최소 한 군데에도 파티션이 없다면 거리두기를 지키지 않은 것이므로 False를 반환한다.
 
  - 이러한 작업을 모두 마쳤음에도 False가 반환되지 않았다면 거리두기를 지킨 것이므로 True를 반환한다.

4. 최종적으로 각 대기실별 거리두기 상황을 담은 result 리스트를 반환한다.

'''
