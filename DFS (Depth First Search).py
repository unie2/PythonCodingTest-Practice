''' DFS implementation example '''

def dfs(graph, v, visited) :
  visited[v] = True # Visit the current node
  print(v, end = ' ')

  for i in graph[v] : # Visit other nodes connected to the current node using a recursive function
    if not visited[i] :
      dfs(graph, i, visited)

graph = [ # Express information that each node is connected to
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9  # Express information about each node visited

dfs(graph, 1, visited)


# result => 1 2 7 6 8 3 4 5
