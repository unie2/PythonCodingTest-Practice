import sys
input = sys.stdin.readline

n = int(input())
dp = [i for i in range(n + 1)]

for i in range(1, n + 1) :
	for j in range(1, i) :
		if j**2 > i :
			break
		if dp[i] > dp[i-j**2] + 1 :
			dp[i] = dp[i-j**2] + 1

print(dp[n])

'''
1. 0부터 n + 1까지 각 인덱스 값을 초기화한 dp 리스트를 정의한다.
2. 2중 for문을 통해 1번째 요소부터 특정 기준값 전까지의 값을 확인하여 이전값의 제곱(j**2) 수가 기준값(i)보다 클 경우 break한다.
3. 1을 제외하고 작은수부터 제곱한 수를 기준값과 비교하여 하나라도 있으면 그 제곱수 값 + 1을 할당한다.
4. 반복문이 모두 종료되면 최종적으로 dp리스트의 n번째 요소를 출력한다.

'''
