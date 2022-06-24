t = int(input())

for tc in range(1, t + 1) :
    a, b = map(int, input().split())
    print('#%d %d' % (tc, a + b))
    
# 1. 각 테스트 케이스마다 두 양수(a, b)를 입력받아 해당 테스트 케이스 번호와 함께 두 수의 합을 출력한다.
