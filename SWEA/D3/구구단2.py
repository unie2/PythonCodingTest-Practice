t = int(input())

for tc in range(1, t + 1) :
    a, b = map(int, input().split())
    if a > 9 or b > 9 :
        print('#%d %d' % (tc, -1))
    else :
        print('#%d %d' % (tc, a * b))
        
'''
1. 각 테스트 케이스마다 입력받은 a와 b 중 하나라도 9보다 크다면 해당 테스트 케이스 번호와 함께 -1을 출력한다.
2. 그렇지 않다면 해당 테스트 케이스 번호와 함께 두 수를 곱한 값을 출력한다.

'''
