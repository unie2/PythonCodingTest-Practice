import copy
# import sys
# input = sys.stdin.readline

def combinations(arr, r) :
    for i in range(len(arr)) :
        if r == 1 :
            yield [arr[i]]
        else :
            for next in combinations(arr[i+1:], r-1) :
                yield [arr[i]] + next

# 적이 남아 있는지 확인
def check() :
    for i in range(n) :
        for j in range(m) :
            if temp[i][j] == 1 :
                return False
    return True

# 적 공격
def attack(arr) :
    enemy = []
    count = 0
    for v in arr :
        # 궁수별로 공격
        get_enemy = []
        for i in range(n) :
            for j in range(m) :
                if temp[i][j] == 1 : # 적이면
                    distance = abs(i-n) + abs(j-v)
                    if distance <= d :
                        get_enemy.append((distance, i, j))

        get_enemy = sorted(get_enemy, key=lambda x: (x[0], x[2]))
        if get_enemy :
            enemy.append(get_enemy[0])

    for e in enemy :
        distance, i, j = e
        if temp[i][j] == 1:
            temp[i][j] = 0 # 적 제거
            count += 1

    return count

def move() :
    for i in range(-1, -n, -1) :
        temp[i] = temp[i-1]
    temp[0] = [0 for _ in range(m)]


n, m, d = map(int, input().split()) # 격자판 행, 열, 공격 거리 제한
# 0은 빈 칸, 1은 적
data = [list(map(int, input().split())) for _ in range(n)]
items = [i for i in range(m)]

result = 0

for value in combinations(items, 3) : # 궁수 배치
    temp = copy.deepcopy(data)
    cnt = 0

    while not check() :
        # 적 공격
        cnt += attack(value)
        # 적 이동
        move()

    result = max(result, cnt)

print(result)

'''
1. n, m, d, 격자판 상태를 입력받고, 궁수를 놓을 위치 번호가 담긴 items 리스트를 정의한다.

2. combinations() 함수를 통해 궁수를 놓을 위치에 대한 모든 경우의 수를 확인하여 제거할 수 있는 적의 최대 수를 갱신해나간다.

3. 각 경우마다 격자판 상태(data)를 temp에 복사하고 적이 격자판에서 모두 없어질 때까지 적을 공격한 수를 누적해나간다. 공격한 이후에는 적을 한 칸씩 아래로 이동시킨다.

4. 각 경우마다 구한 적 공격 수(max(result, cnt))를 갱신한다.

5. 격자판에 적이 아직 존재하는지 판별하는 check() 함수의 작업은 아래와 같다.
  - 격자판에서 1 x 1 크기의 칸을 하나씩 확인하여 그 값이 1일 경우 적이 존재하므로 False를 반환한다.
  - 모든 칸을 확인했을 때 False가 반환되지 않았다면 적이 격자판에 없으므로 True를 반환한다.

6. 적을 공격하는 과정을 구현한 attack() 함수의 작업은 아래와 같다.
  - 공격할 적의 좌표가 담긴 enemy 리스트와 공격한 적의 수를 의미하는 count를 정의한 후 궁수별로 공격을 시작한다.
  - temp격자판의 칸을 하나씩 확인하고, 그 값이 1일 경우 적이 존재하므로 현재 궁수의 좌표와 해당 적의 좌표의 거리(distance)를 구한다.
  - 만약 거리(distance)가 d 이하일 경우 공격할 수 있으므로 get_enemy 리스트에 (거리, 좌표) 형태로 값을 담는다.

  - 이후 get_enemy를 정렬하는데, 이때 거리 -> 열 좌표가 낮은 순으로 정렬을 수행한다.
  - 만약 get_enemy리스트에 값이 존재하면 enemy 리스트에 가장 첫 번째 요소를 추가한다.

  - 궁수 별로 공격할 적이 모두 선정되면 적의 정보를 하나씩 꺼내고, 꺼낸 좌표가 1일 경우 0으로 갱신한 후 count 값을 1 증가시킨다.
    최종적으로 count 값을 반환한다.

7. 적의 위치를 한 칸씩 아래로 이동시키는 move() 함수의 작업은 아래와 같다.
  - 거꾸로 갱신을 시작하며, 위 칸에 존재하는 상태를 현재 칸에 담는다.
  - 가장 윗 행에 존재하는 값들은 모두 0으로 갱신한다.

'''
