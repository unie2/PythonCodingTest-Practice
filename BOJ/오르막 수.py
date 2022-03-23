n = int(input())
dp = [[0] * 10 for i in range(n)]
dp[0] = [1 for i in range(10)]

for i in range(1, n) :
	sum_value = 0
	for j in range(10) :
		for k in range(j + 1) :
			dp[i][j] += dp[i-1][k]
			sum_value += dp[i-1][k]

if n == 1 :
	print(10)
else :
	print(sum_value % 10007)
  
'''
1. 2차원 리스트로 dp 테이블을 정의한다. 범위는 0~9까지 이므로 10으로 설정한다.
2. 첫번째 요소 내 10개의 값은 1로 갱신해준다.
3. 3중 for문을 통해 입력받은 n번째 줄까지 하나의 요소마다 [i-1]번째 줄의 [k]번째(즉, 이전 줄의 현재의 인덱스까지) 값을 누적해나간다.
4. 최종적으로 입력받은 n이 1일 경우 단순히 10을 출력하고, 그렇지 않은 경우에는 문제에서 요구하는 바와 같이 sum_value를 10,007로 나눈 나머지 값을 출력한다.

'''
