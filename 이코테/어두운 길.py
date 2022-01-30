# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x) :
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x :
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b) :
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b


# 노드의 개수와 간선의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1) :
  parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(m) :
  x, y, z = map(int, input().split())
  # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
  edges.append((z, x, y))

# 간선을 비용순으로 정렬
edges.sort()
total = 0 # 전체 가로등 비용

# 간선을 하나씩 확인하며
for edge in edges :
  cost, a, b = edge
  total += cost
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b) :
    union_parent(parent, a, b)
    result += cost

print(total - result)


'''
* 이 문제에서는 가로등이 켜진 도로만을 이용해서, 모든 두 집이 서로 도달이 가능해야 한다는 조건을 제시하고 있다.
  이때 최소한의 비용으로 모든 집을 연결해야 하기 때문에, 이를 통해 전형적인 최소 신장 트리 문제라는 것을 알 수 있다.

* 주어진 입력을 통해서 그래프를 구성한 뒤에 크루스칼 알고리즘을 수행하면 된다.

* 문제에서 요구하는 답은 '절약할 수 있는 최대 금액'이므로 '전체 가로등을 켜는 비용 - 최소 신장 트리를 구성하는 비용'을 출력한다.

'''
