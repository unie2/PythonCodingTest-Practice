t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    result = 0
    for i in range(1, n + 1) :
        if i % 2 == 0 : # 짝수일 경우
            result -= i
        else : # 홀수일 경우
            result += i

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 n을 입력받아 1부터 n까지 반복문을 수행하여 현재 확인하고 있는 값이 짝수일 경우 result 값에서 해당 수를 감소시키고, 홀수일 경우 result 값에서 해당 수를 증가시킨다.
2. 반복 작업이 끝나면 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
