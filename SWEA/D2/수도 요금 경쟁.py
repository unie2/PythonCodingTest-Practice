t = int(input())

for i in range(1, t + 1) :
    p, q, r, s, w = map(int, input().split()) # A사 1리터당 P원, B사 기본 요금, B사 월간 사용량 기준, 초과량에 대한 S원, 한달 간 사용하는 수도의 양 W
    a_result, b_result = 0, 0
    a_result += w * p
    b_result += q
    if w > r :
        b_result += (w - r) * s

    print('#%d %d' % (i, min(a_result, b_result)))
    
'''
1. 각 테스트 케이스마다 p, q, r, s, w 값을 입력받고, a_result 와 b_result 를 0으로 초기화한다.
2. A사는 1리터당 p원의 돈을 지불해야하므로 집에서 한 달간 사용하는 수도의 양(w)과 p를 곱하여 a_result 값에 누적한다.
3. B사는 기본 요금(q)을 먼저 누적한 후 r 리터보다 많은 양을 사용한 경우 초과량(w - r)에 대해 1리터당 s원의 요금을 b_result에 누적한다.
4. 최종적으로 테스트 케이스 번호와 함께 a_result와 b_result 중 최소 값을 출력한다.

'''
