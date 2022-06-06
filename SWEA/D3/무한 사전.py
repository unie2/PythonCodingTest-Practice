t = int(input())

for tc in range(1, t + 1) :
    p = input().rstrip()
    q = input().rstrip()

    if p + "a" != q :
        print('#%d %s' % (tc, 'Y'))
    else :
        print('#%d %s' % (tc, 'N'))
        
# 1. 각 테스트 케이스마다 문자열 p와 q를 입력받은 후, 만약 p에 문자 "a"를 붙인 값이 q와 같지 않다면 p와 q 사이에 다른 단어가 있으므로
#   해당 테스트 케이스 번호와 함께 'Y'를 출력하고, 그렇지 않다면 'N'을 출력한다.
