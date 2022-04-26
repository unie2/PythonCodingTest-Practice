n = int(input())
data = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(1, n + 1) :
    total += sum(data[i])

def solution(x, y, d1, d2) :
    temp = [[0] * (n + 1) for _ in range(n + 1)]
    # 2번 조건
    temp[x][y] = 5
    for i in range(1, d1 + 1) :
        temp[x+i][y-i] = 5
    for i in range(1, d2 + 1) :
        temp[x+i][y+i] = 5
    for i in range(1, d2 + 1) :
        temp[x+d1+i][y-d1+i] = 5
    for i in range(1, d1 + 1) :
        temp[x+d2+i][y+d2-i] = 5

    count = [0] * 5
    # 1번 선거구
    for r in range(1, x + d1) :
        for c in range(1, y + 1) :
            if temp[r][c] == 5 :
                break
            else :
                count[0] += data[r][c]

    # 2번 선거구
    for r in range(1, x + d2 + 1) :
        for c in range(n, y, -1) :
            if temp[r][c] == 5 :
                break
            else :
                count[1] += data[r][c]

    # 3번 선거구
    for r in range(x + d1, n + 1) :
        for c in range(1, y - d1 + d2) :
            if temp[r][c] == 5 :
                break
            else :
                count[2] += data[r][c]

    # 4번 선거구
    for r in range(x + d2 + 1, n + 1) :
        for c in range(n, y - d1 + d2 - 1, -1) :
            if temp[r][c] == 5 :
                break
            else :
                count[3] += data[r][c]

    # 5번 선거구
    count[4] = total - sum(count)
    return max(count) - min(count)

result = int(1e9)
for x in range(1, n + 1) :
    for y in range(1, n + 1) :
        for d1 in range(1, n + 1) :
            for d2 in range(1, n + 1) :
                # 1번 조건
                if x + d1 + d2 > n :
                    continue
                if y - d1 < 1 :
                    continue
                if y + d2 > n :
                    continue

                result = min(result, solution(x, y, d1, d2))

print(result)

'''
1. 입력받은 N개의 줄의 N개의 정수 값을 모두 더하여 total에 저장한다.
2. 4중 for문을 통해 모든 경우의 수를 확인해보며, 문제에서 제시한 1번 조건에 만족한다면 solution() 함수를 호출하여 반환받은 값과 result 값을 비교하여 최솟 값을 result에 갱신한다.
3. solution() 함수 내부 작업은 아래와 같다.
  - 임시로 N x N 크기의 temp 리스트를 만들고, 전달받은 x, y 좌표의 값을 5로 설정한다.
  - 문제에서 제시한 선거구를 나누는 방법의 2번을 바탕으로 반복문을 각 수행하여 해당 좌표의 값을 5로 갱신한다.
  - 각 선거구의 인원을 세기 위해 count 리스트를 정의하고, 문제에서 제시한 방법의 4번을 바탕으로 반복문을 각 수행하여 해당 좌표 값이 5가 아닐 때 그 값을 count[해당 인덱스] 에 누적한다.
  - 1번~4번 선거구는 5번 선거구에 포함되지 않은 구역이므로 5번 선거구의 인구는 total - sum(count) 로 구할 수 있다.
  - 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이를 구하여 반환한다.
4. 최종적으로 최솟값이 담겨 있는 result 값을 출력한다.

'''
