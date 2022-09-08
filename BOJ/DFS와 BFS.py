from collections import deque

def dfs(start) :
    visited[start] = 1 # 방문 처리
    print(start, end=' ')
    for i in range(1, n + 1) :
        if visited[i] == 0 and graph[start][i] == 1 : # 미방문 and 연결되어 있다면
            dfs(i)


def bfs(start) :
    q = deque([start])
    visited[start] = 1

    while q :
        node = q.popleft()
        print(node, end=' ')
        for i in range(1, n + 1) :
            if visited[i] == 0 and graph[node][i] == 1 : # 미방문 and 연결되어 있다면
                q.append(i)
                visited[i] = 1


n, m, v = map(int, input().split()) # 정점 수, 간선 수, 시작 번호
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(v)
print()
visited = [0] * (n + 1)
bfs(v)

'''
1. 정점 수, 간선 수, 시작 번호를 입력받아 특정 노드와 노드의 연결 상태를 나타내는 2차원 graph 리스트와 방문 여부를 나타내는 visited 리스트를 정의한다.

2. 시작 노드를 dfs() 의 매개변수로 하여 함수를 호출하고, dfs() 함수의 작업은 아래와 같다.
  - 전달받은 노드를 방문 처리해주고, 노드 번호를 출력한다.
  - 해당 노드와 연결되어 있는 노드들 중 작은 순서의 노드 번호를 매개변수로 하여 dfs() 함수를 재귀호출한다.

3. dfs() 함수의 작업이 끝나면 방문 여부 리스트(visited)를 다시 초기화해준 뒤 아래와 같은 bfs() 함수의 작업을 수행한다.
  - q에 start를 할당하여 deque를 정의하고, 해당 노드를 방문 처리한다.
  - q가 빌 때까지 노드를 하나씩 꺼내 화면에 출력하고, 해당 노드와 연결된 노드들 중 작은 순서의 노드 번호를 q에 추가하고 방문 처리한다.

'''
