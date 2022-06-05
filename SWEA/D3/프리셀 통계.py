t = int(input())

for tc in range(1, t + 1) :
    n, Pd, Pg = map(int, input().split())

    if Pd != 0 and Pg == 0 :
        print('#%d %s' % (tc, 'Broken'))
    elif Pd != 100 and Pg == 100 :
        print('#%d %s' % (tc, 'Broken'))
    else :
        flag = False
        for i in range(1, n + 1) :
            if (i * Pd) / 100 == (i * Pd) // 100 : # 정수라면
                flag = True
                break

        if flag :
            print('#%d %s' % (tc, 'Possible'))
        else :
            print('#%d %s' % (tc, 'Broken'))
            
'''
1. 각 테스트 케이스마다 n, Pd, Pg를 입력받고, 만약 Pd가 0이 아니고 Pg가 0이라면 Pg가 0%가 될 수 없으므로 'Broken'을 출력한다.
2. 만약 Pd가 100이 아니고 Pg가 100이라면 Pg가 100%가 될 수 없으므로 'Broken'을 출력한다.
3. 1부터 n까지의 수를 확인하여 (i * Pd) / 100​ 의 값이 정수가 될 경우 'Possible'을 출력하고, 정수가 되는 경우가 없다면 'Broken'을 출력한다.

'''
