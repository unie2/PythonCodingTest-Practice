n, m = map(int, input().split())

d = [[0] * m for _ in range(n)] # 방문한 위치를 저장하기 위한 맵 초기화
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 캐릭터의 좌표 값 방문처리

array = []
for i in range(n) :
  array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left() :
  global direction
  direction -= 1
  if direction == -1 :
    direction = 3

count = 1
turn_time = 0
while True :
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  
  if d[nx][ny] == 0 and array[nx][ny] == 0 :
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else :
    turn_time += 1
    
  # 네 방향 모두 갈 수 없을 때
  if turn_time == 4 :
    nx = x - dx[direction]
    ny = y - dy[direction]

    if array[nx][ny] == 0 :
      x = nx
      y = ny
    else :
      break
    turn_time = 0

print(count)
