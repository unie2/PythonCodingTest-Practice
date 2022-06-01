from collections import deque, defaultdict

def bfs(start, cut, wires, n, wire_dict) :
    count = 0
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True

    while q :
        v = q.popleft()
        for next in wire_dict[v] :
            if next == cut :
                continue
            if visited[next] :
                continue
            count += 1
            q.append(next)
            visited[next] = True

    return count

def solution(n, wires) :
    answer = 100000
    # 딕셔너리로 그래프 저장
    wire_dict = defaultdict(set)
    for wire in wires :
        wire_dict[wire[0]].add(wire[1])
        wire_dict[wire[1]].add(wire[0])

    # wire 하나를 끊는 모든 경우의 수
    for wire in wires :
        v1 = wire[0]
        v2 = wire[1]
        diff = abs(bfs(v1, v2, wires, n, wire_dict) - bfs(v2, v1, wires, n, wire_dict))
        answer = min(answer, diff)

    return answer
  
'''
1. 전달받은 wires의 정보를 그래프 형태로 구성하기 위해 wire_dict 딕셔너리를 정의하고 wires의 요소를 하나씩 꺼내 두 번호를 연결한다.

2. bfs() 함수를 통해 wire 하나를 끊는 모든 경우의 수를 확인하여 끊어진 두 구역에 대한 노드 개수의 절대값이 최소가 되도록 한다.

3. bfs() 함수의 작업은 아래와 같다.
  - count를 0으로 초기화시켜주고 방문처리 여부를 담을 visited 리스트를 정의한다.
  - start 값을 deque로 감싸 q를 정의하고 start를 방문 처리(True) 한다.
  - q가 빌 때까지 q에 담겨 있는 요소를 하나씩 꺼내고 딕셔너리에서 연결되어 있는 다음 번호를 가져와 그 번호가 cut가 같을 경우 continue한다.
  - 또한 다음 번호가 이미 방문되어있다면 continue한다.
  - continue 되지 않았다면 count를 1 증가시키고 q에 다음 번호를 담고 방문처리를 수행한다.
  - while문이 종료되면 count 값을 반환한다.

'''
