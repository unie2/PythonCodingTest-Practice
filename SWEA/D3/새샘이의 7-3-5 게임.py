from itertools import combinations

t = int(input())
for tc in range(1, t + 1) :
    data = list(map(int, input().split()))
    result = []
    for value in combinations(data, 3) :
        result.append(sum(value))

    result = list(set(result))
    result.sort(reverse=True)
    print('#%d %d' % (tc, result[4]))
    
'''
1. 각 테스트 케이스마다 입력받은 7개의 정수 중에서 3개의 정수를 도출하여 세 수의 합을 result 리스트에 저장한다.
2. 이후 result 리스트의 중복을 제거하고 내림차순으로 정렬하고, 해당 테스트 케이스 번호와 함께 result리스트의 다섯 번째 요소를 출력한다.

'''
