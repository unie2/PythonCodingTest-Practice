t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    result = f'1/{n} ' * n

    print('#%d %s' % (tc, result))
    
'''
1. 각 테스트 케이스마다 '1/n ' 의 문자열을 n개 붙여 result에 할당한다.
2. 최종적으로 해당 테스트 케이스 번호와 함께 result 문자열을 출력한다.

'''
