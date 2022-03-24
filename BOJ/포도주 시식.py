n = int(input())

wine = []
for i in range(n) :
	wine.append(int(input()))

dp = [0] * n
dp[0] = wine[0]

if n > 1 :
	dp[1] = wine[0] + wine[1]
if n > 2 :
	dp[2] = max(wine[2] + wine[1], wine[2] + wine[0], dp[1])

for i in range(3, n) :
	dp[i] = max(dp[i-1], dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i])

print(dp[n-1])

'''
1. n개의 포도주의 각 양을 입력받아 wine 리스트에 추가한다.
2. wine의 0번째 인덱스 값을 dp 리스트 0번째 요소에 할당한다.
3. 입력받은 n이 1보다 클 경우, dp[1]에 wine[0] 과 wine[1]의 합을 할당한다.
4. 입력받은 n이 2보다 클 경우, 3잔은 연속으로 마실 수 없으므로, wine[2]+wine[1] 과 wine[2]+wine[0] 과 dp[1] 값을 비교하여 가장 큰 값을 dp[2]에 할당한다.
5. 반복문을 통해 dp[3]부터 dp[n-1]까지 값을 할당하는데, dp[i-1] 과 dp[i-3]+wine[i-1]+wine[i] 과 dp[i-2]+wine[i] 값을 비교하여 가장 큰 값을 dp[i]에 할당한다.

'''
