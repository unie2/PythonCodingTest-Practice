from itertools import combinations

t = int(input())
for tc in range(1, t + 1) :
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    result = 0
    for i in range(1, len(data) + 1) :
        for value in combinations(data, i) :
            if sum(value) == k :
                result += 1

    print('#%d %d' % (tc, result))
    
    
'''
1. 각 테스트 케이스마다 n개의 수를 입력받아 data 리스트에 저장한다.
2. itertools.combinations() 를 통해 data 리스트의 요소를 i개씩 뽑고, 뽑은 값들의 합이 k와 같을 경우 result를 1 증가시킨다.
3. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
