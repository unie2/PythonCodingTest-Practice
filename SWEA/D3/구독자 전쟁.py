t = int(input())
result = []

for tc in range(1, t + 1) :
    n, a, b = map(int, input().split())
    max_value = min(a, b)
    sum_value = a + b
    min_value = sum_value - n
    if min_value < 0 :
        min_value = 0

    result.append([max_value, min_value])

for idx, value in enumerate(result) :
    print('#%d %d %d' % (idx + 1, value[0], value[1]))
    
'''
1. 각 테스트 케이스마다 입력받은 a와 b 중 최솟값을 max_value(최댓값)에 할당한다.
2. a + b - n 값을 min_value(최솟값)에 할당하고, min_value가 음수라면 0으로 갱신한다.
3. result 리스트에 [max_value, min_value] 형태로 값을 추가한다.
4. 모든 테스트 케이스 작업을 마치면 enumerate() 를 통해 해당 idx와 함께 최댓값, 최솟값 순으로 출력한다.

'''
