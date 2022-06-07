from math import sqrt

t = int(input())

for tc in range(1, t + 1) :
    a, b = map(int, input().split())
    result = 0

    for i in range(a, b + 1) :
        if str(i) == str(i)[::-1] :
            value = sqrt(i)
            if value == int(value) :
                if str(int(value)) == str(int(value))[::-1] :
                    result += 1

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 a이상 b이하의 수들을 하나씩 확인하면서 만약 해당 수가 팰린드롬이라면 i의 제곱근을 value에 할당한다.
2. 만약 value 값이 정수일 경우 팰린드롬인지 확인하고, 팰린드롬이라면 result 값을 1 증가시킨다.
3. a 이상 b 이하의 수들을 모두 확인하면 최종적으로 해당 테스트 케이스 번호와 함께 result 를 출력한다.

'''
