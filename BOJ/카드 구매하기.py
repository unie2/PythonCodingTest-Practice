import sys
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1) :
	for j in range(1, i + 1) :
		dp[i] = max(dp[i], dp[i-j] + p[j])

print(dp[n])

'''
1. 인덱싱을 위해 입력받은 p 리스트 맨 앞에 0을 넣어주고, dp 리스트를 0으로 초기화 한다.
2. 이중 for문을 통해 각 카드 개수와 지불하는 최대 금액을 구한다.
3. 값 갱신 시, 현재 카드를 지불하는 최대 금액(dp[i])과 이전의 카드를 지불한 최대 금액(dp[i-j])에 j개가 들어있는 카드팩 금액(p[j])을 비교하여 더 큰 값으로 dp[i]를 갱신한다.
4. 최종적으로 dp[n]을 출력해줌으로써 카드 n개를 갖기 위해 지불해야 하는 금액의 최댓값을 출력한다.

'''
