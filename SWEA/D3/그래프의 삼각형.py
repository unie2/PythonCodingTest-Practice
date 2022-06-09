from collections import defaultdict

t = int(input())
for tc in range(1, t + 1) :
    n, m = map(int, input().split())
    data = defaultdict(list)

    for _ in range(m) :
        x, y = map(int, input().split())
        data[x].append(y)
        data[y].append(x)

    result = 0
    for i in range(1, n + 1) :
        for j in range(i + 1, n + 1) :
            for k in range(j + 1, n + 1) :
                if i in data[j] and j in data[k] and k in data[i] :
                    result += 1

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 data 딕셔너리를 생성하고, 입력받은 x, y에 대하여 data[x]에 y를 추가하고, data[y]에 x를 추가한다.
2. 3중 for문을 수행하여 각 상황마다 삼각형을 이루고 있다면 result 값을 1 증가시킨다.
3. 반복문이 끝나면 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
