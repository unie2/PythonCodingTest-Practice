t = int(input())

for tc in range(1, t + 1) :
    p, q = map(float, input().split())
    s1 = (1 - p) * q # 한번
    s2 = p * (1 - q) * q # 두번

    if s1 < s2 :
        print('#%d %s' % (tc, 'YES'))
    else :
        print('#%d %s' % (tc, 'NO'))
        
'''
1. 각 테스트 케이스마다 s1에 (1 - p) * q를 할당하고, s2에 p * (1 - q) * q 를 할당한다.
2. 만약 s1가 s2보다 작다면 해당 테스트 케이스 번호와 함께 'YES'를 출력하고, 그렇지 않다면 'NO'를 출력한다.

'''
