from collections import deque

n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
graph = [[5] * n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
dead = [[list() for _ in range(n)] for _ in range(n)]
for _ in range(m) :
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def spring_summer() :
    # 봄
    for i in range(n) :
        for j in range(n) :
            len_value = len(trees[i][j])
            for k in range(len_value) :
                if graph[i][j] < trees[i][j][k] :
                    for _ in range(k, len_value) :
                        dead[i][j].append(trees[i][j].pop())
                    break
                else :
                    graph[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1

    # 여름
    for i in range(n) :
        for j in range(n) :
            while dead[i][j] :
                graph[i][j] += dead[i][j].pop() // 2

def fall_winter() :
    # 가을
    for i in range(n) :
        for j in range(n) :
            for k in range(len(trees[i][j])) :
                if trees[i][j][k] % 5 == 0 :
                    for l in range(8) :
                        nx = i + dx[l]
                        ny = j + dy[l]
                        if not 0 <= nx < n or not 0 <= ny < n :
                            continue
                        trees[nx][ny].appendleft(1)

            # 겨울
            graph[i][j] += A[i][j]

for i in range(k) :
    spring_summer()
    fall_winter()

result = 0
for i in range(n) :
    for j in range(n) :
        result += len(trees[i][j])

print(result)

'''
1. 각 칸에 대한 양분의 양의 값을 갖는 A리스트, 모든 칸이 5로 초기화된 양분 값을 갖는 graph리스트, 각 나무의 좌표와 나이 정보가 담긴 trees리스트, 죽은 나무 정보를 담는 dead리스트를 구성한다.
2. 입력받은 k번 만큼 반복 수행하여 하나의 반복 작업이 수행될 때마다 spring_summer() 함수와 fall_winter() 함수를 호출한다.
3. spring_summer() 함수에서는 나무 정보를 하나씩 확인하여 해당 나무의 나이가 땅에 존재하는 양분보다 클 경우 먹을 수 없으므로 dead리스트에 추가한다.
4. 반대로 땅에 존재하는 양분보다 작거나 같을 경우 나무가 자신의 나이만큼 양분을 먹고 나이를 1 증가시킨다.
5. 이후 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가될 수 있도록 한다.
6. fall_winter() 함수에서는 현재 확인하고 있는 나무가 5의 배수인지 확인하여 인접한 8개의 칸에 나이가 1인 나무를 추가한다.
7. 이후 땅을 돌아다니면서 땅에 A[i][j] 값만큼의 양분을 추가한다.
8. 이와 같은 반복작업을 모두 마치면 최종적으로 땅에 살아있는 나무의 개수를 구하여 출력한다.

'''
