for tc in range(1, 11) :
    test_case = int(input())
    a, b = map(int, input().split())

    print('#%d %d' % (test_case, a ** b))
    
# 1. 각 테스트 케이스마다 a, b를 입력받아 해당 테스트 케이스 번호와 함께 a의 b 거듭제곱 값을 출력한다.
