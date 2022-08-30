def func(x, y, cnt) :
    global result

    if y >= 10 :
        result = min(result, cnt)
        return
    if x >= 10 :
        func(0, y+1, cnt)
        return

    if data[x][y] == 1 :
        # 색종이 붙여야 함
        for k in range(4, -1, -1) :
            if paper[k] == 5 :
                continue
            if x + k >= 10 or y + k >= 10 :
                continue

            flag = 0
            for i in range(x, x+k+1) :
                for j in range(y, y+k+1) :
                    if data[i][j] == 0 :
                        flag = 1
                        break
                if flag == 1 :
                    break

            if flag == 0 :
                for i in range(x, x+k+1) :
                    for j in range(y, y+k+1) :
                        data[i][j] = 0

                paper[k] += 1
                func(x+k+1, y, cnt + 1)
                paper[k] -= 1

                for i in range(x, x+k+1) :
                    for j in range(y, y+k+1) :
                        data[i][j] = 1
    else :
        func(x+1, y, cnt)


data = [list(map(int, input().split())) for _ in range(10)]
paper = [0 for _ in range(5)]

result = 1e9
func(0, 0, 0)

if result == 1e9 :
    print(-1)
else :
    print(result)
    
'''
1. 10 x 10 크기의 종이 상태를 입력받아 2차원 data 리스트에 저장하고, 5개의 색종이의 각 크기별 개수를 담은 paper 리스트를 정의한다.

2. rseult를 최대값으로 초기화해주고, func() 함수를 수행한 후 result 값을 확인한다.

3. result 값이 여전히 최대값이라면 모두 덮는 것이 불가능하므로 -1을 출력하고, 그렇지 않다면 result를 출력한다.

4. 색종이를 종이에 덮는 func() 함수의 작업은 아래와 같다.
  - 만약 y의 값이 10 이상이라면 상태가 1인 모든 칸을 다 덮었으므로 result 값을 cnt와 비교하여 최솟값으로 갱신한다.
  - 만약 x의 값이 10 이상이라면 다음 열을 확인해야하므로 func(0, y+1, cnt)를 재귀 호출한다.

  - 현재의 좌표(data[x][y])가 1이라면 각 색종이의 개수를 확인한다. (0이라면 다음 좌표 확인)
  - 해당 크기의 색종이의 개수가 5개이거나 해당 크기로 덮을 경우 범위를 벗어나게 된다면 사용할 수 없으므로 continue한다.
  - 사용이 가능한 크기라면 해당 크기의 종이판 상태를 확인하고, 그 과정에서 0이 나올 경우 덮을 수 없으므로 flag를 1로 갱신하고 break한다.
  - flag 값이 0일 경우 해당 크기의 종이판 상태를 모두 0으로 갱신하고, 해당 색종이를 사용했으므로 개수를 1 증가한 뒤 다음 좌표와 cnt+1 값을 매개변수로 하여 func() 함수를 재귀 호출한다.
  - 재귀 호출한 후에는 다른 경우도 확인해봐야 하므로 해당 색종이 사용 횟수를 1 감소하고, 색종이로 덮은 종이의 좌표들도 1로 다시 갱신한다.

'''
