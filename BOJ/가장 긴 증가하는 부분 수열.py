import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = [1] * n

for i in range(n) :
	for j in range(i) :
		if data[j] < data[i] :
			dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

'''
1. 증가하는 수열을 바탕으로 가장 첫번째 요소는 자기 자신 포함하여 1이므로, dp 리스트를 1로 초기화 한다.
2. 이중 for문을 통해 현재 확인하고 있는 값과 그 이전에 있는 값들을 하나씩 확인하여 이전 값이 더 작을 경우 dp[i]와 dp[j]+1 값을 비교하여 더 큰 값을 dp[i]에 갱신한다.
3. 반복문이 모두 종료되면 dp 리스트에서 가장 큰 값을 출력한다.

'''
