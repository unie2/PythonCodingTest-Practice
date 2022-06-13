t = int(input())

for tc in range(1, t + 1) :
    n = int(input())

    if n % 2 == 0 :
        print('#%d %s' % (tc, 'Even'))
    else :
        print('#%d %s' % (tc, 'Odd'))
        
'''
1. 각 테스트 케이스마다 양의 정수를 하나 입력받고, 해당 수가 2로 나누어 떨어지면 짝수이므로 'Even'을 출력한다.
2. 해당 수가 2로 나누어 떨어지지 않는다면 홀수이므로 'Odd'를 출력한다.

'''
