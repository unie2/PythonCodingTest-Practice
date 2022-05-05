from collections import deque
n, m, t = map(int, input().split())
data = [deque(int(x) for x in input().split()) for _ in range(n)]

for tc in range(t) :
    x, d, k = map(int, input().split())
    # 회전 작업 수행
    result = 0
    for i in range(n) :
        result += sum(data[i])
        if (i+1) % x == 0 :
            if d == 0 : # 시계 방향 회전
                data[i].rotate(k)
            else : # 반시계 방향 회전
                data[i].rotate(-k)

    # 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 제외
    if result != 0 :
        remove_value = []
        for i in range(n) :
            for j in range(m-1) :
                if data[i][j] != 0 and data[i][j+1] != 0 and data[i][j] == data[i][j+1] :
                    remove_value.append((i, j))
                    remove_value.append((i, j+1))
            if data[i][0] != 0 and data[i][-1] != 0 and data[i][0] == data[i][-1] :
                remove_value.append((i, 0))
                remove_value.append((i, m-1))

        for j in range(m) :
            for i in range(n-1) :
                if data[i][j] != 0 and data[i+1][j] != 0 and data[i][j] == data[i+1][j] :
                    remove_value.append((i, j))
                    remove_value.append((i+1, j))

        # 원판 갱신
        remove_value = list(set(remove_value))
        for i in range(len(remove_value)) :
            x, y = remove_value[i]
            data[x][y] = 0

        # 없는 경우 : 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고 작은 수에는 1을 더한다.
        if len(remove_value) == 0 :
            sum_value = 0
            zero_count = 0
            for i in range(n) :
                sum_value += sum(data[i])
                zero_count += data[i].count(0)
            avg_value = sum_value / (n * m - zero_count)

            for i in range(n) :
                for j in range(m) :
                    if data[i][j] != 0 and data[i][j] > avg_value :
                        data[i][j] -= 1
                    elif data[i][j] != 0 and data[i][j] < avg_value :
                        data[i][j] += 1
    else :
        break

answer = 0
for i in range(n) :
    answer += sum(data[i])

print(answer)

'''
1. 각 작업마다 x, d, k를 입력받고 회전 작업을 수행한다. 회전 작업은 아래와 같다.
  - result 값에 data[i]에 존재하는 요소들의 합을 누적한다. 이는 이후 작업 중 원판에 수가 남아 있는지 확인하기 위함이다.
  - 현재 확인하고 있는 인덱스가 x의 배수일 경우 d 값을 확인하고, d 값이 0일 경우 시계 방향으로, 1일 경우 반시계 방향으로 회전한다.
2. 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 제외시키는 작업을 수행한다. 작업은 아래와 같다.
  - 현재 확인하고 있는 값과 인접한 위치의 값이 같을 경우 remove_value 리스트에 두 좌표를 추가한다.
3. 정의된 remove_value 리스트를 바탕으로 해당 좌표의 값들을 모두 0으로 갱신한다.
4. 만약 제외시킬 값이 없을 경우, 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
5. 이와 같은 작업이 t번 진행된 후 최종적으로 원판에 적힌 수의 합을 출력한다.

'''
