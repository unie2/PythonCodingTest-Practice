t = int(input())

for tc in range(1, t + 1) :
    min_value = -1
    n, a, b = map(int, input().split())
    for r in range(1, n + 1) :
        c = 1
        while r * c <= n :
            value = a * (abs(r - c)) + b * (n - (r * c))
            if min_value == -1 :
                min_value = value
            else :
                min_value = min(min_value, value)
            c += 1

    print('#%d %d' % (tc, min_value))
    
'''
1. 각 테스트 케이스마다 min_value를 -1로 초기화하고 n, a, b 값을 입력받는다.

2. 1부터 n + 1까지를 반복문의 범위로 설정하고, 그 내부에서 c를 1로 초기화한다.

3. r * c의 값이 n보다 클 때까지 아래의 작업을 반복한다.
  - 문제에서 제시한 식을 계산하여 value에 할당하고, 만약 min_value가 -1일 경우 min_value에 value를 할당한다.
  - min_value의 값이 -1이 아닐 경우 현재의 min_value와 value를 비교하여 더 작은 값을 min_value에 할당한다.
  - 하나의 반복 수행 작업이 끝날 때마다 c를 1 증가시킨다.

4. 최종적으로 해당 테스트 케이스 번호와 함께 min_value를 출력한다.

'''
