# 1일 때 : 0
# 2일 때 : 3
# 3일 때 : 0
# 4일 때 : 11
# 5일 때 : 0

n = int(input())

if n == 1 :
	print(0)
elif n == 2 :
	print(3)
elif n == 3 :
	print(0)
else :
	dp = [0] * (n + 1)
	dp[0] = 1
	dp[2] = 3

	for i in range(4, n + 1) :
		if i % 2 == 0 :
			dp[i] = dp[i-2] * 3
			for j in range(4, i + 1, 2) :
				dp[i] += dp[i-j] * 2

	print(dp[n])
  
'''
1. n을 1씩 증가시키면서 그림을 그려보면 점화식은 아래와 같다.

  dp[2] : 3가지
  dp[4] : dp[2] * 3 + dp[0] * 2
  dp[6] : dp[4] * 3 + dp[2] * 2 + dp[0] * 2

2. 또한, n이 홀수일 경우는 모두 0가지이며, dp[0]은 1로 정의할 수 있다.
3. 반복문을 통해 현재 확인하고 있는 인덱스(i)가 짝수일 경우에만 위 점화식을 적용한다.

'''
