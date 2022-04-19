n, m, h = map(int, input().split())
visited = [[False] * (n + 1) for _ in range(h + 1)]
data = []
for _ in range(m) :
    a, b = map(int, input().split())
    visited[a][b] = True

def check() :
    for i in range(1, n + 1) :
        now = i
        for j in range(1, h + 1) :
            if visited[j][now-1] :
                now -= 1
            elif visited[j][now] :
                now += 1
        if now != i :
            return False
    return True

def dfs(depth, index) :
    global result
    if depth >= result :
        return
    if check() :
        result = depth
        return

    for c in range(index, len(data)) :
        x, y = data[c]
        if not visited[x][y-1] and not visited[x][y+1] :
            visited[x][y] = True
            dfs(depth + 1, c + 1)
            visited[x][y] = False

for i in range(1, h + 1) :
    for j in range(1, n) :
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1] :
            data.append([i, j])

result = 4
dfs(0, 0)

if result < 4 :
    print(result)
else :
    print(-1)
    
'''
1. a와 b를 입력받아 visited 리스트의 방문처리를 통해 사다리 연결을 수행한다.
2. 특정 위치의 양 옆에 사다리가 연결되어 있다면 사다리를 추가로 연결할 수 없기 때문에 연결하는 지점의 방문처리가 되지 않은 위치를 구하고, 해당 좌표를 data 리스트에 추가한다.
3. result 값은 4로 초기화시켜주고, dfs() 함수를 호출한다.
4. dfs() 함수 내부에서는 depth 값을 확인하여 그 값이 result보다 크거나 같을 경우에는 그 다음 경우를 볼 필요가 없으므로 return한다.
5. depth 값이 result값보다 작다면 check() 함수를 호출하여 True를 반환받으면 result 값을 depth 값으로 갱신하고 return 한다.
6. check() 함수 호출로 받은 값이 False라면 반복문을 돌려 사다리를 놓을 수 있는 후보군의 인덱스에 다시 한번 사다리를 놓을 수 있는지 확인하고,
   놓을 수 있다면 사다리를 놓은 후 dfs() 함수를 재귀호출한다. 호출 후에는 해당 좌표의 방문여부를 다시 False로 갱신해준다.
7. 추가적으로, check() 함수를 통해 모든 열에 대하여 현재 i번째 열의 도착점이 i번째인지 확인한다.
   해당 열에 대하여 왼쪽에 사다리가 놓여있다면 왼쪽으로 이동하고, 혀냊 위치에 사다리가 놓여있다면 오른쪽으로 이동한다.
   이후 출발점과 도착점을 확인하여 다르다면 False를, 같다면 True를 반환한다.
8. 최종적으로 result 값을 확인하고, 그 값이 3보다 큰 값이면 -1을 출력한다.


'''
