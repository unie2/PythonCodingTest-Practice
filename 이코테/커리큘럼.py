from collections import deque
import copy

v = int(input()) # 노드(강의)의 개수 입력
indegree = [0] * (v + 1) # 진입차수 초기화
graph = [[] for i in range(v + 1)] # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
time = [0] * (v + 1) # 각 강의 시간 초기화

# 방향 그래프의 모든 간선 정보 입력
for i in range(1, v + 1) :
  data = list(map(int, input().split()))
  time[i] = data[0]
  for x in data[1:-1] :
    indegree[i] += 1
    graph[x].append(i)

# 위상 정렬 알고리즘 수행
def topology_sort() :
  result = copy.deepcopy(time) # 리스트 값 복제
  q = deque()

  for i in range(1, v + 1) :
    # 진입차수가 0인 노드를 큐에 삽입
    if indegree[i] == 0 :
      q.append(i)

  while q : # 큐가 빌 때까지
    # 큐에서 원소 꺼내기
    now = q.popleft()
    
    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for i in graph[now] :
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1
      
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0 :
        q.append(i)

  for i in range(1, v + 1) :
    print(result[i])

topology_sort()
