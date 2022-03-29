import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = [i for i in data]

for i in range(1, n) :
	dp[i] = max(dp[i], dp[i-1] + data[i])

print(max(dp))

'''
1. 입력받은 데이터를 이루는 data 리스트를 통해 dp리스트을 추가로 정의한다.
2. 연속된 몇 개의 수를 선택해야하므로, 반복문을 통해 dp[i]와 dp[i-1]+data[i]를 비교하여 더 큰 값을 dp[i]에 갱신한다. 여기서 dp[i-1]은 이전에 갱신되었기 때문에 단순히 dp[i-1] + data[i]를 연산하여 해결할 수 있다.
3. 최종적으로 dp 리스트에서 가장 큰 값을 출력한다.

'''
