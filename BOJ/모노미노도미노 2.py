n = int(input())
blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]

result = 0

def move_blue(t, x) :
    global blue
    y = 1
    if t == 1 or t == 2 :
        while True :
            if y + 1 > 5 or blue[x][y + 1] : # 범위를 벗어나거나 블록이 있다면
                blue[x][y] = 1
                if t == 2 :
                    blue[x][y-1] = 1
                break
            y += 1
    else :
        while True :
            if y + 1 > 5 or blue[x][y+1] != 0 or blue[x+1][y+1] != 0 :
                blue[x][y], blue[x+1][y] = 1, 1
                break
            y += 1

    check_blue()

    for j in range(2) :
        for k in range(4) :
            if blue[k][j] :
                remove_blue(5)
                break

def check_blue() :
    global result
    for j in range(2, 6) :
        cnt = 0
        for k in range(4) :
            if blue[k][j] :
                cnt += 1

        if cnt == 4 :
            remove_blue(j)
            result += 1

def remove_blue(index) :
    for j in range(index, 0, -1) :
        for k in range(4) :
            blue[k][j] = blue[k][j-1]
    for j in range(4) :
        blue[j][0] = 0

def move_green(t, y) :
    global green
    x = 1
    if t == 1 or t == 3 :
        while True :
            if x + 1 > 5 or green[x+1][y] :
                green[x][y] = 1
                if t == 3 :
                    green[x-1][y] = 1
                break
            x += 1
    else :
        while True :
            if x + 1 > 5 or green[x+1][y] or green[x+1][y+1] :
                green[x][y], green[x][y+1] = 1, 1
                break
            x += 1

    check_green()

    for j in range(2) :
        for k in range(4) :
            if green[j][k] :
                remove_green(5)
                break

def check_green() :
    global result
    for j in range(2, 6) :
        cnt = 0
        for k in range(4) :
            if green[j][k] :
                cnt += 1

        if cnt == 4 :
            remove_green(j)
            result += 1

def remove_green(index) :
    for j in range(index, 0, -1) :
        for k in range(4) :
            green[j][k] = green[j-1][k]
    for j in range(4) :
        green[0][j] = 0

for _ in range(n) :
    t, x, y = map(int, input().split())
    move_blue(t, x)
    move_green(t, y)

blue_count, green_count = 0, 0
for i in range(4) :
    for j in range(2, 6) :
        if blue[i][j] : # 블록이 존재하면
            blue_count += 1

for i in range(2, 6) :
    for j in range(4) :
        if green[i][j] : # 블록이 존재하면
            green_count += 1

print(result)
print(blue_count + green_count)

'''
1. 4 x 6 크기의 파란 구역(blue) 리스트와 6 x 4 크기의 초록 구역(green) 리스트를 정의한다.

2. t, x, y를 입력받고, t와 x를 매개변수로 하여 move_blue() 함수를 호출한 후 t와 y를 매개변수로 하여 move_green() 함수를 호출한다.

3. 이후 파란 구역에 존재하는 블록의 수와 초록 구역에 존재하는 블록의 수를 구한다.

4. 최종적으로 블록을 모두 놓았을 때 얻은 점수(result)와 blue_count + green_count 값을 출력한다.

5. 블록을 이동시키는 move_blue() 함수의 작업은 아래와 같다.
  - 전달받은 t가 1이거나 2일 경우 y 값을 1씩 증가시켜 블록을 놓을 위치를 구한다.
  - 만약 보드의 범위를 벗어나거나 다음 칸에 이미 블록이 있을 경우 현재의 위치 값을 1로 갱신한다.
    또한, t값이 2일 경우 이전 위치(x, y-1) 또한 블록이 들어가야하므로 1로 갱신해주고 break한다.
  - t가 3일 경우도 마찬가지로 y 값을 1씩 증가시켜 블록을 놓을 위치를 구한다.
  - 만약 보드의 범위를 벗어나거나 다음 칸에 이미 블록이 있을 경우 현재의 위치와 아래 위치(x+1, y)를 1로 갱신해준다.
  
  - 위 작업을 수행하고 check_blue() 함수를 호출하여 제거해야할 블록이 있는지 확인한다. 있다면 remove_blue() 함수를 통해 제거한다.
  - 이후 연한색 범위(0열, 1열)에 블록이 존재할 경우 remove_blue() 함수를 통해 가장 우측에 존재하는 블록들을 제거하고 오른쪽으로 한칸씩 이동시킨다.

6. 제거해야 할 블록이 있는지 확인하는 check_blue() 함수의 작업은 아래와 같다.
  - 특정 열에 대한 4개의 행이 모두 블록으로 꽉찼을 경우(cnt == 4) remove_blue() 함수를 통해 해당 블록들을 제거한다.

7. 블록을 제거하고 위치를 한 칸씩 옮겨주는 remove_blue() 함수의 작업은 아래와 같다.
  - 전달받은 index값부터 거꾸로 하여 해당 위치의 값을 이전 값으로 갱신해준다.
  - 가장 좌측에 존재하는 0번째 열들(blue[i][0])의 값을 0으로 갱신한다.

8. 초록 구역의 작업 또한 인덱스만 변경해주고 파란 구역의 작업과 동일하다.

'''
