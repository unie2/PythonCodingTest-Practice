t = int(input())

for tc in range(1, t + 1) :
    l, u, x = map(int, input().split())
    result = 0
    if x < l :
        result = l - x
    elif x > u :
        result = -1

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 l, u, x 값을 입력받는다.
2. result를 0으로 초기화하고, 만약 x가 l보다 작다면 result에 l - x 값을 할당한다.
3. 만약 x가 u보다 크다면 result에 -1을 할당한다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
