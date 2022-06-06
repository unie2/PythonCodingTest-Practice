t = int(input())

for tc in range(1, t + 1) :
    d, l, n = map(int, input().split()) # D(1 + n*L%)
    result = 0
    cnt = 0

    while cnt < n :
        damage = d * (1 + cnt * (l / 100))
        result += damage
        cnt += 1
    
    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 cnt를 0으로 초기화시켜 cnt가 n과 같아질 때까지 while문을 수행한다.
2. 각 반복 수행 작업에서 문제에서 제시한 바와 같이 (d * (1 + cnt * (l / 100)) 을 연산하여 result에 누적하고, cnt를 1 증가시킨다.
3. while문 수행이 끝나면 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
