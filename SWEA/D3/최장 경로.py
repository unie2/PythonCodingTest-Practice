def dfs(i, count) :
    global max_value

    for j in range(1, n + 1) :
        if not visited[j] and data[i][j] :
            visited[j] = 1
            dfs(j, count + 1)
            visited[j] = 0
    if count > max_value :
        max_value = count

t = int(input())

for tc in range(1, t + 1) :
    n, m = map(int, input().split())
    data = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [0] * (n + 1)
    max_value = 0
    for _ in range(m) :
        x, y = map(int, input().split())
        data[x][y] = 1
        data[y][x] = 1

    for i in range(1, n + 1) :
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print('#%d %d' % (tc, max_value))
    
'''
1. 각 테스트 케이스마다 (n + 1) x (n + 1) 크기의 2차원 리스트 data를 정의하고 방문여부를 확인하기 위해 visited 리스트도 정의한다.

2. m개의 간선 정보를 입력받아 두 정점이 연결되어 있음을 알 수 있도록 해당 좌표의 값을 1로 갱신한다.

3. 1부터 n + 1까지를 반복문의 범위로 설정하며, visited[i]를 방문처리(1) 해주고 dfs() 함수를 호출한 뒤 방문처리를 다시 해제(0)한다.

4. dfs() 함수의 작업은 아래와 같다.
  - i와 경로 상에 등장하는 정점의 개수를 구하기 위한 count 값을 매개변수로 받는다.
  - 1부터 n + 1까지를 반복문의 범위로 설정하며, 만약 j가 방문처리 되어 있지않고 두 정점이 연결되어 있다면 j를 방문처리해주고 dfs() 함수를 재귀 호출한 뒤 방문처리를 해제한다.
  - 만약 count 값이 max_value 값보다 크다면 max_value 값을 count로 갱신한다.

5. 최종적으로 해당 테스트 케이스 번호와 함께 max_value 값을 출력한다.

'''
