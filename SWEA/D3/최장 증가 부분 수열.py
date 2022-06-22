t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = 1

    for i in range(1, n) :
        for j in range(i-1, -1, -1) :
            if data[i] > data[j] :
                dp[i] = max(dp[i], dp[j])
        dp[i] += 1

    print('#%d %d' % (tc, max(dp)))
    
'''
1. 각 테스트 케이스마다 n개의 수를 입력받아 data 리스트에 저장하고, n개의 0으로 초기화된 dp 리스트를 정의한 후 dp[0] 을 1 로 갱신한다.
2. 2중 for문을 통해 dp 값을 갱신해 나가는데, 만약 data[i]가 data[j]보다 크다면 증가 부분 수열이므로 dp[i]와 dp[j] 중 최댓값을 dp[i]에 갱신한다.
3. 내부 반복문이 끝날 때마다 dp[i]의 값을 1 증가시킨다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 dp 리스트의 최댓값을 출력한다.

'''
