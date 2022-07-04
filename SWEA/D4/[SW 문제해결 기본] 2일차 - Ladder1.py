for _ in range(1, 11) :
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    for i in range(100) :
        if data[0][i] == 1 : # 시작
            x, y = 0, i
            while x != 99 :
                x += 1
                if y > 0 and data[x][y-1] == 1 :
                    while y > 0 and data[x][y-1] == 1 :
                        y -= 1
                elif y < 99 and data[x][y+1] == 1 :
                    while y < 99 and data[x][y+1] == 1 :
                        y += 1

            if data[x][y] == 2 :
                result = i
                break

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 100 x 100 크기의 2차원 data 리스트에 값을 입력받아 저장한다.

2. 반복문을 통해 data[0][i]를 확인하고, 만약 그 값이 1일 경우 x가 99가 될 때까지 아래와 같은 작업을 반복한다.
  - x 값을 1 증가시킨다.
  - 만약 왼쪽에 갈 수 있는 길(1)이 있을 경우 1이 아닐 때까지 y를 1 감소시켜 왼쪽으로 이동한다.
  - 왼쪽에 갈 수 있을 길이 없고 만약 오른쪽에 갈 수 있는 길(1)이 잇을 경우 1이 아닐 때가지 y를 1 증가시켜 오른쪽으로 이동한다.

3. x가 99일 때 만약 data[x][y]가 2일 경우 result에 i 값을 할당하고 break 한다.

4. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
