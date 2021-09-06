from collections import deque

def bfs(i, j) :
  queue = deque()
  queue.append((i, j))

  while queue :
    i, j = queue.popleft()

    for k in range(4) :
      result_x = i + go_x[k]
      result_y = j + go_y[k]

      if result_x<0 or result_x>=n or result_y<0 or result_y>=m :
        continue

      if graph[result_x][result_y] == 0:
        continue
        
      if graph[result_x][result_y] == 1 :
        graph[result_x][result_y] = graph[i][j] + 1
        queue.append((result_x, result_y))

  return graph[n-1][m-1]

n, m = map(int, input().split())

graph = []
for z in range(n) :
  graph.append(list(map(int, input())))

go_x = [-1, 1, 0, 0]
go_y = [0, 0, -1, 1]

print(bfs(0, 0))
