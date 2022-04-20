# 0 : ->, 1 : ↑, 2 : <-, 3 : ↓

n = int(input())
graph = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n) :
    y, x, d, g = map(int, input().split())
    graph[x][y] = 1

    # 커브 리스트
    curve = [d]
    for j in range(g) :
        for k in range(len(curve)-1, -1, -1) :
            curve.append((curve[k] + 1) % 4)

    # 드래곤 커브
    for j in range(len(curve)) :
        x += dx[curve[j]]
        y += dy[curve[j]]
        if not 0 <= x < 101 or not 0 <= y < 101 :
            continue
        graph[x][y] = 1

result = 0
for i in range(100) :
    for j in range(100) :
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1 :
            result += 1

print(result)

'''
1. 동 북 서 남의 방향을 갖는 dx, dy 리스트를 구성한다.
2. 문제에서 요구한 바와 같이 x축은 가로방향, y축은 세로방향이므로 y, x, d, g 순으로 값을 입력받아 할당한다.
3. 입력받은 좌표 graph[x][y] 에 값을 1로 갱신하여 해당 꼭짓점을 드래곤 커브의 일부로 설정한다.
4. 커브 리스트를 생성하는데, 초기에는 입력받은 d 값을 리스트 형태로 할당하고, 반복문을 통해 (curve[k]+1) % 4의 값을 추가해준다.
   (방향은 0, 1, 2, 3 총 네 가지이므로 4로 나눈 나머지 값을 추가하도록 한다.)
5. 반복문을 통해 드래곤 커브를 구성하는데, 각 x와 y의 좌표를 구하여 범위를 벗어나지 않는다면 해당 좌표의 값을 1로 갱신한다.
6. 이와 같은 작업을 n번 수행해준 후, 최종적으로 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 구하여 출력한다.

'''
