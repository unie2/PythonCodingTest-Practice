from collections import defaultdict

def bfs(num) :
    next = [num]
    while True :
        queue = next[:]
        temp_q = queue[:]
        next = []
        while queue :
            q = queue.pop(0)
            if q in info :
                for value in info[q] :
                    if visited[value] == 0 :
                        visited[value] = 1
                        next.append(value)
        if len(next) == 0 :
            return max(temp_q)

for tc in range(1, 11) :
    n, start = map(int, input().split())
    data = list(map(int, input().split()))
    visited = [0] * (max(data) + 1)
    info = defaultdict(list)

    for i in range(0, n-1, 2) :
        if data[i+1] not in info[data[i]] :
            info[data[i]].append(data[i+1])
    visited[start] = 1

    print('#%d %d' % (tc, bfs(start)))
    
'''
1. 각 테스트 케이스마다 입력받은 n개의 값(data)에서 {from, to} 쌍으로 확인하여 info 딕셔너리를 정의한다.

2. 방문 여부 확인을 위해 visited 리스트를 초기화하고 start 정점에 대해 방문처리(1)한다.

3. 해당 테스트 케이스 번호와 함께 bfs() 함수를 호출하여 반환받은 값을 출력한다.

4. bfs() 함수의 작업은 아래와 같다.
  - 함수로 전달받은 num 값을 리스트 형태로 하여 next에 할당한다.
  - while문을 통해 수행되며, queue에 next를 복사하고 temp_q에 queue를 복사한 후 next 리스트를 초기화한다.
  - queue가 빌 때까지 whlie문을 수행하며, queue에 존재하는 값을 하나씩 꺼내 q에 담고, 만약 q가 info 딕셔너리에 존재한다면
    q 정점에서 갈 수 있는 정점(value)을 꺼낸다.
  - 만약 갈 수 있는 정점(value)이 아직 방문되지 않았다면 방문처리를 하고 next 리스트에 추가한다.
 
  - queue에 대한 작업을 모두 마치면 next에 존재하는 값의 개수를 확인하는데, 그 값이 0일 경우 temp_q에서 가장 큰 값을 반환한다.

'''
