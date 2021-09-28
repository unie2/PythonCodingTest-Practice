# 특정 원소가 속한 집합 찾기
def find_parent(parent, x) :
  # 해당 노드가 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x :
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b) :
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b

v, e = map(int, input().split()) # 노드(집), 간선(길)의 개수 입력
parent = [0] * (v + 1) # 부모 테이블 초기화

edges = []
result = 0

# 부모테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1) :
  parent[i] = i

# 모든 간선에 대한 정보 입력
for _ in range(e) :
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort() # 오름차순 정렬
last = 0

for edge in edges :
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b) :
    union_parent(parent, a, b)
    result += cost
    last = cost

print(result - last) # 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선 빼기
