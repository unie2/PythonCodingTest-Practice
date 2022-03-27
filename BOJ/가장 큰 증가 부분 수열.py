import sys
input = sys.stdin.readline

a = int(input())
data = list(map(int, input().split()))
dp = [i for i in data]

for i in range(a) :
	for j in range(i) :
		if data[j] < data[i] :
			dp[i] = max(dp[i], dp[j] + data[i])

print(max(dp))

'''
1. 입력받은 값들을 이루는 리스트 dp 테이블을 추가로 정의한다.
2. 2중 for문을 통해 특정 값을 기준으로 그 이전값까지 값을 비교하고, 이전에서 확인하고 있는 값이 기준값보다 작을 경우 dp[i] (기준값)와 dp[j] + data[i] (이전값과의 합)을 비교하여 더 큰 값을 dp[i]에 갱신한다.
3. 반복문이 모두 종료되면 dp 리스트에서 가장 큰 값을 출력한다.

'''
