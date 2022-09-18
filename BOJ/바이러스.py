# https://www.acmicpc.net/problem/2606

from collections import defaultdict, deque

def bfs(num) :
    global result

    flag[num] = True
    q = deque()
    q.append(num)

    while q :
        value = q.popleft()
        for v in dict[value] :
            if flag[v] == False :
                flag[v] = True
                result += 1
                q.append(v)

    print(result)

total = int(input())
flag = [False] * (total + 1)
n = int(input())

dict = defaultdict(list)
for _ in range(n) :
    a, b = map(int, input().split())
    dict[a].append(b)
    dict[b].append(a)

result = 0
bfs(1)

'''
1. 컴퓨터의 개수(total)를 입력받아 각 컴퓨터의 방문 여부를 담은 flag 리스트를 정의하고, dict 딕셔너리를 정의한다.

2. 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍을 n번 입력받아 각각 dict 딕셔너리에 연결한다.

3. bfs() 함수를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 구하여 출력한다. bfs() 함수의 작업은 아래와 같다.
  - 가장 처음 전달받은 1번 컴퓨터의 flag 값을 True로 갱신하고 deque()를 정의하여 1번 컴퓨터를 q에 추가한다.
  - q가 빌 때까지 아래와 같은 작업을 수행한다.
    - q에 존재하는 값을 하나 꺼내 value에 할당하고, value에 연결되어 있는 컴퓨터를 한대씩 확인한다. (dict[value])
    - 확인하고 있는 컴퓨터가 아직 방문되지 않았으면 방문처리하고 result를 1증가시킨 후 q에 해당 컴퓨터 번호를 추가한다.
  - q에 존재하는 컴퓨터들을 모두 확인한 후 최종적으로 result 값을 출력한다.

'''
