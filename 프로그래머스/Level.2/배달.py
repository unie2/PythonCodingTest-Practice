from collections import defaultdict, deque

def solution(n, road, k) :
    graph = defaultdict(list)
    for v1, v2, dis in road :
        graph[v1].append((v2, dis))
        graph[v2].append((v1, dis))

    visited = [0 for _ in range(n + 1)]
    q = deque([(1, 0)])
    visited[1] = 1

    while q :
        node, dis = q.popleft()

        for v, w in graph[node] :
            if dis + w <= k and (not visited[v] or dis + w <= visited[v]) :
                q.append((v, dis + w))
                visited[v] = dis + w

    answer = n + 1 - visited.count(0)

    return answer
  
'''
1. 전달받은 road 내 요소를 하나씩 꺼내 graph 딕셔너리의 key 값을 v1로, value 값을 (v2, dis) 형태로 삽입한다.
   양방향으로 움직일 수 있으므로 마찬가지로 key 값을 v2로, value 값을 (v1, dis) 형태로 삽입한다.

2. 방문 여부를 확인할 수 있도록 visited 리스트를 생성하고 큐에 (1번 노드, 거리) 형태로 삽입한 뒤 1번 노드의 방문 여부 값을 1로 갱신한다.

3. 큐가 빌 때까지 큐에서 노드 번호와 거리를 꺼내고, 아래와 같은 작업을 수행한다.
  - 해당 노드에 대응하는 딕셔너리 값을 하나씩 꺼낸다.
  - 만약 dis + w 값이 k보다 작거나 같고, 딕셔너리에서 꺼낸 노드가 방문 처리되지 않았거나 dis + w가 꺼낸 노드의 방문 여부 값보다 작거나 같을 경우
   큐에 (딕셔너리에서 꺼낸 노드, dis + w) 형태로 삽입하고 방문 여부 값에도 dis + w로 갱신한다.

4. n + 1 (0 노드도 포함하기 때문) 에서 visited 리스트의 0의 개수를 뺀 값을 answer에 할당하여 반환한다.

'''
