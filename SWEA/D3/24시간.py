t = int(input())

for tc in range(1, t + 1) :
    a, b = map(int, input().split())
    hour = a + b

    print('#%d %d' % (tc, hour % 24))
    
# 1. 각 테스트 케이스마다 입력받은 a와 b를 더하고 24로 나눈 나머지 값을 해당 테스트 케이스 번호와 함께 출력한다.
