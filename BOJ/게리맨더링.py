from collections import defaultdict, deque

def combinations(arr, r) :
    for i in range(len(arr)) :
        if r == 1 :
            yield [arr[i]]
        else :
            for next in combinations(arr[i+1:], r-1) :
                yield [arr[i]] + next

def bfs(arr) :
    start = arr[0]
    q = deque([start])
    visited = [start]

    sum_value = 0
    while q :
        node = q.popleft()
        sum_value += person[node]
        for next in dict[node] :
            if next not in visited and next in arr :
                q.append(next)
                visited.append(next)

    return sum_value, len(visited)

n = int(input())
person = [0] + list(map(int, input().split()))

dict = defaultdict(list)
result = 1e9

for i in range(1, n + 1) :
    value = list(map(int, input().split()))
    dict[i].extend(value[1:])

for i in range(1, n // 2 + 1) :
    for value in combinations(range(1, n + 1), i) :
        sum_1, len_1 = bfs(value)
        sum_2, len_2 = bfs([i for i in range(1, n+1) if i not in value])
        if len_1 + len_2 == n :
            result = min(result, abs(sum_1 - sum_2))

if result == 1e9 :
    print(-1)
else :
    print(result)
    
'''
1. 각 구역에 존재하는 인구의 수를 person리스트에 담고, 구역을 연결하기 위한 dict 딕셔너리와 result 값을 초기화한다.

2. 각 구역과 해당 구역과 연결된 다른 구역들을 입력받아 dict 딕셔너리에 저장한다.

3. 1부터 n의 절반까지를 반복문의 범위로 지정하여 구역을 두 개로 나눠 각 sum_1(인구의 합), len_1(선거구1의 구역 개수) 그리고 sum_2(인구의 합), len_2(선거구2의 구역 개수)를 구한다.

4. 만약 두 선거구의 총 구역 개수가 n과 같다면 모든 구역에 대하여 잘 방문했으므로 result 값을 갱신한다.(최소값으로)

5. 최종적으로 result 값을 확인하여 그 값이 가장 초기에 정의한 값(1e9)과 같다면 -1을, 그렇지 않다면 result 값을 출력한다.

6. 특정 선거구의 총 인구를 구하기 위한 bfs() 함수의 작업은 아래와 같다.
  - arr 리스트의 0번째 요소를 시작 지점으로 하기 위해 start에 할당하고, deque로 정의된 q에 start를 할당한 후 방문여부를 확인하기 위한 visited 리스트에도 start를 할당한다.
  - q가 빌 때까지 가장 앞에 존재하는 요소를 꺼내(node) sum_value에 해당 구역(node)에 존재하는 인구 수를 누적한다.
  - 해당 구역과 연결된 다른 구역들을 확인하고, 만약 다음 구역이 아직 방문되지 않았고 arr 리스트에 존재한다면(같은 선거구임을 의미) q와 visited에 다음 구역(next)를 추가한다.
  - 해당 선거구의 모든 구역을 확인하는 작업이 끝나면 sum_value(총 인구 수)와 vistied의 개수(구역의 개수)를 반환한다.

'''
