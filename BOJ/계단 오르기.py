import sys
input = sys.stdin.readline

n = int(input())
stair = [0]
for _ in range(n) :
	stair.append(int(input()))

if n == 1 :
	print(stair[1])
else :
	dp = [0] * (n + 1)
	dp[1] = stair[1]
	dp[2] = stair[1] + stair[2]

	for i in range(3, n + 1) :
		dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])

	print(dp[n])
  
  
'''
1. stair 리스트의 0번째 요소는 0으로 초기화하고, 입력받은 n개의 수를 stair에 추가한다.
2. 만약 입력받은 n이 1일 경우 단순히 stair의 1번째 요소를 출력한다.
3. 그렇지 않을 경우 dp리스트를 정의하고, 1번째 요소에 stair[1]을, 2번째 요소에 stair[2]을 할당한다.
4. 반복문을 통해 dp리스트의 3번째 요소부터 값을 갱신해 나아간다.
5. 갱신 시, 연속된 세 개의 계단을 모두 밟으면 안되므로, dp[i-3]+stair[i-1]+stair[i] 와 dp[i-2]+stair[i]를 비교하여 더 큰 값으로 갱신한다.
6. 반복문이 종료되면 최종적으로 dp리스트의 n번째 요소를 출력한다.

'''
