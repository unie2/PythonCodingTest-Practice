from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
q = deque()
data = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m) :
    r, c, mi, s, d = map(int, input().split())
    data[r-1][c-1].append([mi, s, d])
    q.append([r-1, c-1])

for _ in range(k) :
    temp = []
    for _ in range(len(q)) :
        x, y = q.popleft()
        for _ in range(len(data[x][y])) :
            m, s, d = data[x][y].popleft()
            nx = (s * dx[d] + x) % n
            ny = (s * dy[d] + y) % n
            q.append([nx, ny])
            temp.append([nx, ny, m, s, d])

    for x, y, m, s, d in temp :
        data[x][y].append([m, s, d])
    for i in range(n) :
        for j in range(n) :
            if len(data[i][j]) > 1 :
                nm, ns, even, odd, flag = 0, 0, 0, 0, 0
                for idx, [m, s, d] in enumerate(data[i][j]) :
                    nm += m
                    ns += s
                    if idx == 0 :
                        if d % 2 == 0 :
                            even = 1
                        else :
                            odd = 1
                    else :
                        if even == 1 and d % 2 == 1 :
                            flag = 1
                        elif odd == 1 and d % 2 == 0 :
                            flag = 1

                nm //= 5
                ns //= len(data[i][j])
                data[i][j] = deque()
                if nm != 0 :
                    for idx in range(4) :
                        if flag == 0 :
                            nd = 2 * idx
                        else :
                            nd = 2 * idx + 1
                        data[i][j].append([nm, ns, nd])

result = 0
for i in range(n) :
    for j in range(n) :
        if data[i][j] :
            for m, s, d in data[i][j] :
                result += m

print(result)

'''
1. 인접한 8개의 칸에 대하여 각 좌표를 dx, dy에 정의한다.
2. 좌표(r, c), 질량(mi), 속력(s), 방향(d)을 입력받아 data리스트의 해당 좌표의 값으로 [mi, s, d]를 추가하고, 큐에도 해당 좌표를 추가한다.
3. 입력받은 k만큼 반복 수행하며, 큐에서 좌표를 꺼내고, data리스트 내 해당 좌표에서 m, s, d 값을 꺼내온다.
4. 꺼내온 값들을 바탕으로 자신의 방향(d)으로 속력(s)만큼 이동하는 nx, ny를 구하여 큐에 추가하고, temp리스트에 [nx, ny, m, s, d]를 추가한다.
5. 이러한 작업이 끝나면 temp리스트의 요소들을 하나씩 확인하여 data리스트 해당 좌표에 [m, s, d]를 추가한다.
6. 이동이 모두 끝난 뒤, 파이어볼이 2개 있는 칸에서는 아래와 같이 작업한다.
  - 합쳐진 파이어볼 질량의 합(nm), 합쳐진 파이어볼 속력의 합(ns), 짝수 개수(even), 홀수 개수(odd), 모두 홀수이거나 짝수인지 확인할 수 있는 flag값을 선언한다.
  - enumerate()를 통해 data[i][j] 요소를 확인하여 m을 nm에, s를 ns에 누적한다.
  - idx를 확인하여 가장 처음 확인한 값이라면 d의 값이 짝수인지 홀수인지 판별하고, 짝수라면 even에 1을, 홀수라면 odd에 1을 할당한다.
  - 가장 처음 확인하는 작업이 아니라면 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수인지 확인하고, 만족하지 않을 경우 flag 값을 1로 갱신한다.
  - 누적된 질량(nm)을 5로 나눈 값으로 갱신하고, 누적된 속력(ns)을 합쳐진 파이어볼의 개수(len(data[i][j])로 나눈 값으로 갱신한다.
  - 질량이 0이 아닐 경우 flag값을 확인하여 그 값이 0이라면 방향을 0, 2, 4, 6으로 정의하고, 1이라면 1, 3, 5, 7로 정의한다.
  - data[i][j]에 각 방향을 포함하여 추가한다. ([nm, ns, nd])
7. 최종적으로 남아있는 파이어볼 질량의 합을 result 값에 누적하여 출력한다.

'''
