t = int(input())

for tc in range(1, t + 1) :
    n, m = map(int, input().split())
    u = 2 * m - n
    t = m - u

    print('#%d %d %d' % (tc, u, t))
    
# 1. 각 테스트 케이스마다 유니콘의 마리 수와 트윈혼의 마리 수를 구하여 해당 테스트 케이스 번호와 함께 출력한다.
