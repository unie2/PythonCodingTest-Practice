t = int(input())
dp = [0] * 101

for _ in range(t) :
	n = int(input())
	def solution(n) :
		if n == 1 or n == 2 or n == 3 :
			return 1
		if dp[n] != 0 :
			return dp[n]
		dp[n] = solution(n-2) + solution(n-3)
		return dp[n]

	print(solution(n))
  
'''
1. 첫 10개의 숫자(1, 1, 1, 2, 2, 3, 4, 5, 7, 9) 를 확인해보면 아래와 같은 규칙을 도출해낼 수 있다.
  dp[n] = dp[n-2] + dp[n-3]

2. 2. 그러므로, n이 1 혹은 2 혹은 3 일 경우 1을 반환하고 dp[n]이 이미 갱신된 상태라면 그대로 반환한다.  또한, 모든 조건문에 해당되지 않는다면 위 점화식과 재귀호출을 통해 dp[n]을 갱신한다.

'''
