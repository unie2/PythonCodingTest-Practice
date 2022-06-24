t = int(input())

for tc in range(1, t + 1) :
    a, b = map(int, input().split())
    result = (a // b) ** 2

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 a, b를 입력받고, a를 b로 나눈 몫의 제곱 값을 result에 할당한다. (직접 그림을 그려보면 쉽게 식을 구할 수 있다.)
2. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
