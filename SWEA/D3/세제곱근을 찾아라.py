t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    result = round(pow(n, 1/3))

    if result ** 3 == n :
        print('#%d %d' % (tc, result))
    else :
        print('#%d %d' % (tc, -1))
        
'''
1. 각 테스트 케이스마다 입력받은 n의 세제곱근을 구하여 반올림처리를 해준 뒤 result에 할당한다.
   여기서 64의 경우 3.9999999999999996가 나오므로 반올림 처리를 해주어야 한다.

2. result 값을 세제곱한 값과 n이 같을 경우 해당 테스트 케이스 번호와 함께 result를 출력하고, 그렇지 않을 경우 -1을 출력한다.

'''
