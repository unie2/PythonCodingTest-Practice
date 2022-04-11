def solution(x, y, d) :
    global result
    if data[x][y] == 0 :
        data[x][y] = 2
        result += 1
    for i in range(4) :
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if data[nx][ny] == 0 :
            solution(nx, ny, nd)
            return
        d = nd

    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if data[nx][ny] == 1 :
        return
    solution(nx, ny, d)

n, m = map(int, input().split())
r, c, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
solution(r, c, d)

print(result)

'''
1. dx, dy 리스트를 통해 북쪽, 동쪽, 남쪽, 서쪽 순으로 방향을 정의한다.
2. solution() 함수 내부에서 현재의 위치를 확인하여 그 값이 0일 경우 청소함으로써 값을 2로 갱신한 후 result를 1증가시킨다.
3. 전달받은 d에 3을 더하고 4로 나눈 나머지 값(왼쪽 방향)을 구하여 이 값을 통해 좌표(nx, ny)를 구한다.
4. 해당 좌표 값이 0일 경우 재귀호출을 통해 청소를 계속해서 진행한다.
5. 네 방향 모두 이동할 수 없다면 현재 방향에 2를 더하여 4로 나눈 나머지 값(뒤쪽 위치)을 구한다.
6. 뒤쪽 방향 또한 벽일 경우 return하고, 이동할 수 있다면 재귀호출을 통해 다음 좌표에 대한 처리를 진행한다.
7. 함수 처리가 종료되면 최종적으로 로봇 청소기가 청소하는 칸의 개수를 의미하는 result 값을 출력한다.

'''
