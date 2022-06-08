t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    result = 0
    for _ in range(n) :
        p, x = map(float, input().split())
        result += p * x

    print(f'#{tc} {result:.6f}')
    
'''
1. 각 테스트 케이스마다 입력받은 p와 x를 곱하여 result에 누적한다.
2. n개의 작업을 모두 마치면 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 소수점 6자리까지 출력한다.

'''
