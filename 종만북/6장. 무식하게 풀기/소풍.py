''' 풀이 1 '''
import sys
input = sys.stdin.readline

def countPairings(n, isFriend, visited) :
  if (sum(visited) == len(visited)) : # 모두 True(1)일 경우
    return 1
  for i in range(n) :
    if (not visited[i]) :
      break
  firstFree = i
  result = 0
  for pairWith in range(firstFree + 1, n) :
    if (not visited[pairWith] and isFriend[firstFree][pairWith]) :
      visited[firstFree] = visited[pairWith] = True
      result += countPairings(n, isFriend, visited)
      visited[firstFree] = visited[pairWith] = False
  return result

c = int(input())
for _ in range(c) :
  n, m = map(int, input().split())
  visited = [False] * n
  isFriend = [[0] * n for _ in range(n)]
  listed = list(map(int, input().split()))
  for i in range(m) :
    u = listed[2*i]
    v = listed[2*i + 1]
    isFriend[u][v] = isFriend[v][u] = 1
  
  print(countPairings(n, isFriend, visited))
  
  
''' 풀이 2 '''
import sys
input = sys.stdin.readline

def dfs(start, friend) :
  if not friend : # friend값이 0일 경우
    return 1
  result = 0

  for i in range(start, n) :
    if not visited[i] :
      for j in range(i+1, n) :
        if not visited[j] and isFriend[i][j] :
          visited[i] = visited[j] = True
          result += dfs(i, friend - 2)
          visited[i] = visited[j] = False

  return result

c = int(input())
for _ in range(c) :
  n, m = map(int, input().split())
  visited = [False] * n
  isFriend = [[False] * n for _ in range(n)]
  listed = list(map(int, input().split()))

  for i in range(0, len(listed), 2) :
    isFriend[listed[i]][listed[i+1]] = True
    isFriend[listed[i+1]][listed[i]] = True

  print(dfs(0, n))
