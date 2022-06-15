t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = []
    for _ in range(n) :
        data.append(int(input()))

    ships = []
    result = 0
    for i in range(1, len(data)) :
        if data[i] in ships :
            continue
        diff = data[i] - 1
        for j in range(diff + 1, data[-1] + 1, diff) :
            ships.append(j)
        result += 1

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력받은 n개의 값을 data 리스트에 저장한다.
2. 1번째 요소부터 끝까지 data 리스트의 요소를 확인하는데, 해당 값이 ships 리스트에 존재한다면 continue 한다.
3. ships에 존재하지 않는 다면 해당 수에서 1을 빼어 (1일 차에서 며칠 후에 즐거운 날인지 구함) diff에 할당한다.
4. diff + 1부터 마지막 날 + 1 까지를 반복문의 범위로 설정하고 diff 단위로 하여 ships 리스트에 j를 추가한다.
5. ships 리스트에 j를 추가하는 반복 작업이 종료되면 result 를 1 증가시킨다.
6. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
