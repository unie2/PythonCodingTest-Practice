''' BFS implementation example '''

from collections import deque 

def bfs(graph, start, visited) :
  queue = deque([start]) # Using deque library
  visited[start] = True # Visit the current node

  while queue :
    v = queue.popleft() # Pull one element from queue
    print(v, end = ' ')

    for i in graph[v] : # # Insert unvisited elements that connected to into the queue.
      if not visited[i] :
        queue.append(i)
        visited[i] = True

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

visited = [False] * 9 # Express information about each node visited

bfs(graph, 1, visited)


# result => 1 2 3 8 7 4 5 6
