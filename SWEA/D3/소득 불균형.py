t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = list(map(int, input().split()))
    sum_value = sum(data)
    avg_value = sum_value / n

    result = 0
    for p in data :
        if p <= avg_value :
            result += 1

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력받은 n개의 수의 평균 값을 구한다.
2. data 리스트의 요소를 하나씩 확인하여 해당 수가 평균 값(avg_value) 이하일 경우에만 result 값을 1 증가시킨다.
3. 모든 요소에 대한 확인 작업을 마치면 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
