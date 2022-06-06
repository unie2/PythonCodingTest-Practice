t = int(input())

for tc in range(1, t + 1) :
    n = input()
    a, b = 1, 1

    for value in n :
        if value == 'L' :
            b = a + b
        elif value == 'R' :
            a = a + b

    print('#%d %d %d' % (tc, a, b))
    
'''
1. 각 테스트 케이스마다 문자열을 입력받고, 문자(value)를 하나씩 확인하여 그 값이 'L'일 경우 b를 a + b로 갱신하고, 'R'일 경우 a를 a + b로 갱신한다.
2. 모든 문자에 대한 작업을 마치면 최종적으로 해당 테스트 케이스 번호와 함께 a와 b를 출력한다.

'''
