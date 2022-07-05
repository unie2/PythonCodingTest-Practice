for _ in range(1, 11) :
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    min_value = 1e9
    result = 0
    for i in range(100) :
        if data[0][i] == 1 : # 시작
            x, y = 0, i
            cnt = 0
            while x != 99 :
                x += 1
                cnt += 1
                if y > 0 and data[x][y-1] == 1 :
                    while y > 0 and data[x][y-1] == 1 :
                        y -= 1
                        cnt += 1
                elif y < 99 and data[x][y+1] == 1 :
                    while y < 99 and data[x][y+1] == 1 :
                        y += 1
                        cnt += 1

            if min_value > cnt :
                min_value = cnt
                result = i

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 100 x 100 크기의 2차원 data 리스트에 값을 입력받아 저장한다.

2. 최단 거리를 의미하는 min_value를 1e9로 초기화하고 최단 거리를 가지는 위치를 담을 result 값을 초기화한다.

3. 반복문을 통해 data[0][i]를 확인하고, 만약 그 값이 1일 경우 cnt를 0으로 초기화한 후 x가 99가 될 때까지 아래와 같은 작업을 반복한다.
  - x 값을 1 증가시킨다.
  - 만약 왼쪽에 갈 수 있는 길(1)이 있을 경우 1이 아닐 때까지 y를 1 감소시켜 왼쪽으로 이동하고 cnt를 1 증가시킨다..
  - 왼쪽에 갈 수 있을 길이 없고 만약 오른쪽에 갈 수 있는 길(1)이 잇을 경우 1이 아닐 때가지 y를 1 증가시켜 오른쪽으로 이동하고 cnt를 1 증가시킨다.

4. 만약 cnt가 min_value 보다 작을 경우 min_value에 cnt를 할당하고 result에 i를 할당한다.

5. 모든 위치에서의 최단 거리를 확인하는 작업을 마치면 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
