def dfs(num) :
    if num == 99 :
        return True
    for i in data[num] :
        if not visited[i] :
            visited[i] = True
            if dfs(i) :
                return True
 
for _ in range(10) :
    tc, n = map(int, input().split())
    data = {i: [] for i in range(100)}
    edges = list(map(int, input().split()))
    visited = {i: False for i in range(100)}
 
    for i in range(0, len(edges), 2) :
        data[edges[i]] += [edges[i+1]]
 
    visited[0] = True
    if dfs(0) :
        print('#%d %d' % (tc, 1))
    else :
        print('#%d %d' % (tc, 0))
        
'''
1. 각 테스트 케이스마다 입력받은 edges 리스트를 통해 data[edges[i]]에 edges[i+1]을 담아 연결시킨다.

2. 출발점이 0이므로 visited[0]을 True로 갱신하여 방문처리를 수해앟ㄴ다.

3. dfs() 함수를 호출하여 만약 반환받은 값이 True라면 해당 테스트 케이스 번호와 함께 1을 출력하고, 그렇지 않다면 0을 출력한다.

4. dfs() 함수의 작업은 아래와 같다.
  - 전달받은 num 값이 99(도착점)일 경우 True를 반환한다.
  - data[num]에 연결된 정점을 하나씩 가져오고, 방문처리가 되지 않았다면 visited[i]를 True로 갱신함으로써 방문처리를 해준 뒤 dfs() 함수에 i를 전달하여 재귀 호출한다.
  - 재귀 호출하여 반환받은 값이 True일 경우 True를 반환한다.

'''
