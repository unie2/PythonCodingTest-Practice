t = int(input())

for tc in range(1, t + 1) :
    n, m = map(int, input().split())
    m = list(map(int, bin(m)[2:]))
    m.reverse()

    if m[:n].count(1) == n :
        print('#%d %s' % (tc, 'ON'))
    else :
        print('#%d %s' % (tc, 'OFF'))
        
'''
1. 각 테스트 케이스마다 입력받은 m을 이진수로 변환하고 앞에 표현된 '0b'를 제거한 후 거꾸로 변환한다.
2. 만약 0번째 요소부터 시작하여 n개의 요소가 모두 1이라면 해당 테스트 케이스 번호와 함께 'ON'을 출력한다.
3. 그렇지 않을 경우 해당 테스트 케이스 번호와 함께 'OFF'를 출력한다.

'''
