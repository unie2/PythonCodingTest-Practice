t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = list(int(input()) for _ in range(n))
    avg_value = sum(data) // n

    result = 0
    for d in data :
        if d > avg_value :
            result += d - avg_value

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력받은 n개의 정수형의 평균(avg_value)을 구한다.
2. data 리스트에 존재하는 값을 하나씩 꺼내, 만약 그 값(d)이 avg_value보다 크다면 (d - avg_value) 값을 result에 누적한다.
3. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
