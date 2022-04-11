from collections import deque

def left(num, direction) :
    if num < 0 :
        return
    if data[num][2] != data[num+1][6] :
        left(num-1, -direction)
        data[num].rotate(direction)

def right(num, direction) :
    if num > 3 :
        return
    if data[num][6] != data[num-1][2] :
        right(num+1, -direction)
        data[num].rotate(direction)

data = []
for _ in range(4) :
    data.append(deque(input()))

k = int(input())
k_value = [list(map(int, input().split())) for _ in range(k)]

for i in range(k) :
    num, direction = k_value[i][0] - 1, k_value[i][1]

    left(num-1, -direction)
    right(num+1, -direction)
    data[num].rotate(direction)

score = 0
if data[0][0] == '1' :
    score += 1
if data[1][0] == '1' :
    score += 2
if data[2][0] == '1' :
    score += 4
if data[3][0] == '1' :
    score += 8


print(score)

'''
1. 입력받은 톱니바퀴의 번호와 방향을 하나씩 확인하여 왼쪽 톱니바퀴와 오른쪽 톱니바퀴를 확인하고, 정의된 방향으로 회전한다.
2. 왼쪽 톱니바퀴가 있을 경우 전달받은 번호의 오른쪽 톱니와 오른쪽 톱니바퀴의 왼쪽 톱니를 비교하여 다르다면 left() 함수를 재귀호출하고, 전달받은 방향으로 회전한다.
3. 오른쪽 톱니바퀴가 있을 경우 전달받은 번호의 왼쪽 톱니와 왼쪽 톱니바퀴의 오른쪽 톱니를 비교하여 다르다면 right() 함수를 재귀호출하고, 전달받은 방향으로 회전한다.
4. 회전 작업을 모두 마치면 네 개의 톱니바퀴의 각 첫번째 값(12시 방향)을 확인하여 그 값이 1일 경우 문제에서 요구하는 점수를 score에 누적한다.

'''
