t = int(input())

for tc in range(1, t + 1) :
    d, h, m = map(int, input().split())
    result = 0
    result += m - 11
    result += (h - 11) * 60
    result += (d - 11) * 24 * 60

    if result < 0 :
        result = -1

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 result를 0으로 초기화 한 후 아래와 같이 작업한다.
  - 분 : (m - 11) 값을 result에 누적한다.
  - 시 : (h - 11) 값을 60으로 곱하여 분 단위로 result에 누적한다.
  - 일 : (d - 11) 값을 24로 곱하여 시간 단위로 변환하고 60을 곱하여 분 단위로 하여 result에 누적한다.

2. 만약 result 값이 0보다 작다면 소개팅 약속 시간 전에 차인 것이므로 result 값을 -1로 갱신한다.

3. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
