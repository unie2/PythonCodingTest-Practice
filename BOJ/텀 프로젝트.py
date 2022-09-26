# https://www.acmicpc.net/problem/9466

import sys
sys.setrecursionlimit(10 ** 8)

def dfs(num) :
    global success
    visited[num] = True
    cycle.append(num)
    target = select[num]

    if visited[target] == True :
        if target in cycle :
            success += cycle[cycle.index(target):]
        return
    else :
        dfs(target)

t = int(input())
for _ in range(t) :
    n = int(input())
    select = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    success = []

    for i in range(1, n + 1) :
        if visited[i] == False :
            cycle = []
            dfs(i)


    print(n - len(success))
    

'''
1. 재귀 깊이를 늘림으로써 오류를 예방한다. (sys.setrecursionlimit())
 
2. 선택된 학생들의 번호(select) 리스트와 방문 여부 확인(visited) 리스트를 정의한다.
 
3. 1번부터 n번까지 하나씩 확인하는데, 해당 번호가 방문하지 않았다면 cycle 리스트를 정의하고 dfs() 함수를 호출한다.
 
4. 1번부터 n번까지의 번호를 모두 확인한 후 최종적으로 n - success의 길이 값(프로젝트 팀에 속하지 못한 학생들 수)을 출력한다.
 
5. dfs() 함수의 작업은 아래와 같다.
  - 전달받은 num의 방문 여부를 True로 갱신한다.
  - cycle 리스트에 num을 추가하고 num이 선택한 번호를 가져와 target에 할당한다.
  - 만약 target이 이미 방문했다면 cycle리스트에 target이 있는지 확인하고, 있다면 사이클이므로 사이클이 발생하는 구간부터만 팀을 이루어 success 리스트에 추가한다.
  - 만약 target이 아직 방문하지 않았다면 dfs() 함수에 target 값을 매개변수로 하여 재귀호출한다.

'''
