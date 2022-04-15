from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)
result = 0

while True :
    # 1단계 수행
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    # 2단계 수행
    if sum(robot) : # 로봇이 존재한다면
        for i in range(n-2, -1, -1) :
            if robot[i] == 1 and robot[i+1] == 0  and belt[i+1] >= 1 :
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1
        robot[-1] = 0
    # 3단계 수행
    if robot[0] == 0 and belt[0] >= 1 :
        robot[0] = 1
        belt[0] -= 1

    result += 1
    # 4단계 수행
    if belt.count(0) >= k :
        break

print(result)

'''
1. 입력받은 벨트(belt)와 로봇(robot)을 deque를 사용하여 구성한 후 while문을 통해 반복 수행한다.
2. 1단계 : rotate(1)을 통해 벨트와 로봇을 한 칸 회전시키고 로봇의 마지막 인덱스는 로봇을 내리는 위치이므로 0으로 설정한다.
3. 2단계 : 로봇이 존재한다면 내리는 위치 이전부터 올리는 위치까지를 반복문의 범위로 잡아 값을 하나씩 확인한다.
          만약 현재 위치에 로봇이 있고 다음 위치로 이동할 수 있으며, 다음 위치의 내구도가 1 이상 남아 있을 경우 로봇을 다음 위치로 이동시키고 이동시킨 위치의 내구도를 1 감소시킨다.
4. 3단계 : 올리는 위치에 로봇이 없고 내구도가 1 이상이라면 해당 위치에 로봇을 올린다.
5. 위와 같은 작업을 수행한 후 result를 1 증가시킨다.
6. 4단계 : 내구도가 0인 칸의 개수가 입력받은 k 이상일 경우 반복문을 종료시키고 result 값을 출력한다.

'''
