import copy

def permutations(arr, r) :
    for i in range(len(arr)) :
        if r == 1 :
            yield [arr[i]]
        else :
            for next in permutations(arr[:i] + arr[i+1:], r - 1) :
                yield [arr[i]] + next

n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
order = [list(map(int, input().split())) for _ in range(k)]

result = 1e9

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 회전 순서 결정
for value in permutations(order, k) :
    temp = copy.deepcopy(data)
    for r, c, s in value :
        for i in range(s) :
            top = [r-s+i-1, c-s+i-1]
            bottom = [r+s-i-1, c+s-i-1]
            nx, ny = top
            tmp = temp[nx][ny]

            for i in range(4) :
                while True :
                    nx = nx + dx[i]
                    ny = ny + dy[i]
                    if not (nx >= top[0] and nx <= bottom[0] and ny >= top[1] and ny <= bottom[1]) :
                        nx = nx - dx[i]
                        ny = ny - dy[i]
                        break
                    tmp, temp[nx][ny] = temp[nx][ny], tmp

    for row in temp :
        sum_value = sum(row)
        result = min(result, sum_value)

print(result)


'''
1. n x m 크기의 2차원 배열 상태를 data 리스트에 담고, k개의 (r, c, s) 값을 order 리스트에 담는다.

2. permutations() 함수를 통해 데이터의 조합을 구해 회전 순서를 결정하고, 각 경우마다 data 리스트를 복사하여 배열을 회전한다.
  - 아래 사진의 형태로 시계 방향으로 회전할 수 있도록 top, bottom을 정의하고, tmp에 초기 값을 할당한다.
  - (동, 남, 서, 북) 순서로 데이터들을 갱신해나간다.
  - while문 내부에서는 다음 좌표 값을 구하고, 그 값이 범위를 벗어나지 않으면 이전 값에 temp[nx][ny]를, 현재의 temp[nx][ny]에 이전 값을 할당한다.
  - 범위를 벗어난다면 다음 방향으로 설정하여 확인해야 하므로, 갱신된 nx, ny 값을 다시 되돌리고 break한다.

3. 회전 작업을 완료한 후 갱신된 2차원 배열의 각 행에 있는 모든 수의 합 중 최솟값을 구해 result에 할당한다.

4. 모든 조합에 대한 작업을 완료하면 최종적으로 result 값을 출력한다.

'''
