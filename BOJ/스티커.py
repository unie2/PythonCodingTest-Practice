import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t) :
	n = int(input())
	dp = [list(map(int, input().split())) for _ in range(2)]

	if n == 1 :
		print(max(dp[0][0], dp[1][0]))
	else :
		dp[0][1] += dp[1][0]
		dp[1][1] += dp[0][0]
		for i in range(2, n) :
			dp[0][i] += max(dp[1][i-1], dp[1][i-2])
			dp[1][i] += max(dp[0][i-1], dp[0][i-2])

		print(max(dp[0][n-1], dp[1][n-1]))
    
'''
1. n이 1일 경우 스티커 두개가 위아래로 서로 인접해 있기 때문에 단순히 두 위치의 값 중 더 큰 값을 출력한다.
2. n이 2 이상일 경우 dp[0][1]에 왼쪽 대각선 아래에 있는 값을 더하고, dp[1][1] 또한 왼쪽 대각선 위에 있는 값을 더한다.
3. 반복문을 통해 2부터 n까지 값을 채워나가는데, 0번째 줄의 특정 위치에 dp[1][i-1] 와 dp[1][i-2] 중 더 큰 값을 더한다.
4. 마찬가지로 1번째 줄의 특정 위치 또한 dp[0][i-1] 와 dp[0][i-2] 중 더 큰 값을 더한다.
5. 반복문이 종료되면 0번째 줄 최종 값과 1번째 줄 최종 값 중 더 큰 값을 출력한다.

'''
