t = int(input())

for i in range(1, t + 1) :
    n = int(input())
    speed = 0
    distance = 0
    for _ in range(n) :
        command = list(map(int, input().split()))
        if command[0] == 1 :
            speed += command[1]
        elif command[0] == 2 :
            if speed > command[1] :
                speed -= command[1]
            else :
                speed = 0
        distance += speed

    print('#%d %d' % (i, distance))
    
'''
1. 각 테스트 케이스마다 n을 입력받고 속도(speed)와 거리(distance)를 0으로 초기화한다.
2. n번의 작업을 수행하는데, 각 작업마다 command를 리스트 형태로 입력받아 아래와 같이 처리한다.
  - command의 첫 요소가 가속(1)일 경우 speed에 두 번째 요소를 누적한다.
  - command의 첫 요소가 감속(2)일 경우 현재 속도(speed) 값이 두 번째 요소(command[1]) 값보다 클 경우 해당 값만큼 감소시킨다.
  - 만약 현재 속도(speed) 값이 두 번째 요소 값보다 작을 경우 음수가 될 수 없도록 speed 값을 0으로 갱신한다.
  - 이와 같은 하나의 작업이 끝나면 속도(speed) 값을 거리(distance)에 누적시킨다.
3. n번의 작업이 모두 끝나면 해당 테스트 케이스 번호와 함께 거리(distance)를 출력한다.

'''
