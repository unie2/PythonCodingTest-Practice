t = int(input())

for tc in range(1, t + 1) :
    h, w = map(int, input().split()) # 높이, 넓이
    data = []
    car_x, car_y = 0, 0
    car_dir = ''
    for i in range(h) :
        temp = list(input())
        data.append(temp)
        for j in range(len(temp)) :
            if temp[j] in ['^', 'v', '<', '>'] :
                car_x, car_y = i, j
                car_dir = temp[j]

    n = int(input()) # 입력의 개수
    order = list(input())
    for i in range(n) :
        if order[i] == 'S' : # Shoot
            if car_dir == '^' : # 위쪽 방향을 바라보고 있다면
                for j in range(car_x-1, -1, -1) :
                    if data[j][car_y] == '*' : # 벽돌일 경우
                        data[j][car_y] = '.' # 평지로 변환
                        break
                    elif data[j][car_y] == '#' : # 강철일 경우
                        break
            elif car_dir == 'v' : # 아래쪽 방향을 바라보고 있다면
                for j in range(car_x+1, h) :
                    if data[j][car_y] == '*' :
                        data[j][car_y] = '.'
                        break
                    elif data[j][car_y] == '#' :
                        break
            elif car_dir == '<' : # 왼쪽 방향을 바라보고 있다면
                for j in range(car_y-1, -1, -1) :
                    if data[car_x][j] == '*' :
                        data[car_x][j] = '.'
                        break
                    elif data[car_x][j] == '#' :
                        break
            elif car_dir == '>' : # 오른쪽 방향을 바라보고 있다면
                for j in range(car_y+1, w) :
                    if data[car_x][j] == '*' :
                        data[car_x][j] = '.'
                        break
                    elif data[car_x][j] == '#' :
                        break
        elif order[i] == 'U' : # 방향을 위쪽으로 바꾸고, 이동
            car_dir = '^'
            nx = car_x - 1
            if not (0 <= nx < h) :
                data[car_x][car_y] = car_dir
                continue
            if data[nx][car_y] == '.' : # 평지라면
                data[car_x][car_y] = '.'
                car_x = nx
            data[car_x][car_y] = car_dir

        elif order[i] == 'D' : # 방향을 아래쪽으로 바꾸고, 이동
            car_dir = 'v'
            nx = car_x + 1
            if not (0 <= nx < h) :
                data[car_x][car_y] = car_dir
                continue
            if data[nx][car_y] == '.' :
                data[car_x][car_y] = '.'
                car_x = nx
            data[car_x][car_y] = car_dir

        elif order[i] == 'L' : # 방향을 왼쪽으로 바꾸고, 이동
            car_dir = '<'
            ny = car_y - 1
            if not (0 <= ny < w) :
                data[car_x][car_y] = car_dir
                continue
            if data[car_x][ny] == '.' :
                data[car_x][car_y] = '.'
                car_y = ny
            data[car_x][car_y] = car_dir

        elif order[i] == 'R' : # 방향을 오른쪽으로 바꾸고, 이동
            car_dir = '>'
            ny = car_y + 1
            if not (0 <= ny < w) :
                data[car_x][car_y] = car_dir
                continue
            if data[car_x][ny] == '.' :
                data[car_x][car_y] = '.'
                car_y = ny
            data[car_x][car_y] = car_dir


    print('#%d' % tc, end=' ')
    for i in range(h) :
        print(''.join(data[i]))
        
'''
1. 각 테스트 케이스마다 전차의 위치를 찾아 car_x, car_y에 좌표를 할당하고 전차의 방향을 car_dir에 할당한다.

2. 입력 정보를 하나씩 확인하여 아래와 같이 작업한다.
  - 입력이 'S'일 경우 각 방향에 맞는 다음 좌표를 확인하고, 다음 좌표가 벽돌 혹은 강철일 경우 break한다. 
    또한, 만약 다음 좌표가 벽돌일 경우에는 해당 좌표를 평지로 변한다.
  - 입력이 'U'일 경우 전차의 방향을 위쪽으로 바꾸고, 다음 좌표가 평지일 경우 해당 좌표로 이동시킨다.
  - 입력이 'D'일 경우 전차의 방향을 아래쪽으로 바꾸고, 다음 좌표가 평지일 경우 해당 좌표로 이동시킨다.
  - 입력이 'L'일 경우 전차의 방향을 왼쪽으로 바꾸고, 다음 좌표가 평지일 경우 해당 좌표로 이동시킨다.
  - 입력이 'R'일 경우 전차의 방향을 오른쪽으로 바꾸고, 다음 좌표가 평지일 경우 해당 좌표로 이동시킨다.

3. 입력 정보에 대한 작업을 모두 수행하면 최종적으로 정의된 게임 맵의 상태(data)를 출력한다.

'''
