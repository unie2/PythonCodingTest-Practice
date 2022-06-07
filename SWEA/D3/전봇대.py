t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = []
    result = 0

    for _ in range(n) :
        a, b = map(int, input().split())
        if data :
            for da, db in data :
                if (a < da and b > db) or (a > da and b < db) :
                    result += 1
        data.append((a, b))

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 n개의 (a, b)를 입력받고, 각 입력 후 만약 data 리스트에 요소가 존재한다면 data 리스트에 존재하는 (da, db)를 꺼내 확인한다.
2. 만약 (1)a가 da보다 작고 b가 db보다 크거나  (2) a가 da보다 크고 b가 db보다 작다면 result 값을 1 증가시킨다.
3. data 리스트에 입력받은 (a, b)를 추가한다.
4. 반복 작업을 모두 수행하면 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
