from collections import deque

# 테스트 케이스만큼 반복
for tc in range(int(input())) :
  # 노드의 개수 입력 받기
  n = int(input())
  # 모든 노드에 대한 진입차수는 -으로 초기화
  indegree = [0] * (n + 1)
  # 각 노드의 연결된 간선 정보를 담기위한 인접 행렬 초기화
  graph = [[False] * (n + 1) for i in range(n + 1)]

  # 작년 순위 정보 입력
  data = list(map(int, input().split()))
  # 방향 그래프의 간선 정보 초기화
  for i in range(n) :
    for j in range(i + 1, n) :
      graph[data[i]][data[j]] = True
      indegree[data[j]] += 1

  # 올해 변경된 순위 정보 입력
  m = int(input())
  for i in range(m) :
    a, b = map(int, input().split())
    # 간선의 방향 뒤집기
    if graph[a][b] :
      graph[a][b] = False
      graph[b][a] = True
      indegree[a] += 1
      indegree[b] -= 1
    else :
      graph[a][b] = True
      graph[b][a] = False
      indegree[a] -= 1
      indegree[b] += 1
  
  # 위상 정렬(Topology Sort) 시작
  result = [] # 알고리즘 수행 결과를 담을 리스트
  q = deque() # 큐 기능을 위한 deque 라이브러리 사용

  # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, n + 1) :
    if indegree[i] == 0 :
      q.append(i)

  certain = True # 위상 정렬 결과가 오직 하나인지의 여부
  cycle = False # 그래프 내 사이클이 존재하는지 여부

  # 정확히 노드의 개수만큼 반복
  for i in range(n) :
    # 큐가 비어 있다면 사이클이 발생했다는 의미
    if len(q) == 0 :
      cycle = True
      break
    # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
    if len(q) >= 2 :
      certain = False
      break
    # 큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
    for j in range(1, n + 1) :
      if graph[now][j] :
        indegree[j] -= 1
        # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
        if indegree[j] == 0 :
          q.append(j)
    
  # 사이클이 발생하는 경우 (일관성이 없는 경우)
  if cycle :
    print("IMPOSSIBLE")
  # 위상 정렬 결과가 여러 개인 경우
  elif not certain :
    print("?")
  # 위상 정렬을 수행한 결과 출력
  else :
    for i in result :
      print(i, end=' ')
    print()
    
    
'''
* '정해진 우선순위에 맞게 전체 팀들의 순서를 나열해야 한다.'는 점에서 위상 정렬 알고리즘을 떠올릴 수 있어야 한다.

* 위상 정렬 수행 후 '자기보다 낮은 등수를 가진 팀을 가리키도록' 방향 그래프를 만들고, 상대적인 순위가 바뀌게 되는 경우에 해당 간선의 방향을 반대로 변경한다.

* 이후에 위상 정렬을 다시 수행하는데, 위상 정렬 수행 과정에서 큐에서 노드를 뽑을 때 큐의 원소가 항상 1개로 유지되는 경우에만 고유한 순위가 존재하는 것으로 이해할 수 있다.

* 그러므로 위상 정렬 소스코드에서 매 시점마다 큐의 원소가 0개이거나, 2개 이상인지를 체크한다.

'''
