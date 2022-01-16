n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n) :
  for j in range(0, i) :
    if array[j] < array[i] :
      dp[i] = max(dp[i], dp[j]+1)

# 열외시켜야 하는 병사의 최소 수를 출력
print(n - max(dp))


'''
* '가장 긴 증가하는 부분 수열' : 하나의 수열이 주어졌을 때 값들이 증가하는 형태의 가장 긴 부분 수열을 찾는 문제이다.
  예를 들어 하나의 수열 array = {10, 20, 10, 30, 20, 50}가 있다고 하자. 이때 가장 긴 증가하는 부분 수열은
  {10, 20, 30, 50}이 될 것이다. 'D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이'라고 정의하면,
  가장 긴 증가하는 부분 수열을 계산하는 점화식은 다음과 같다.
  모든 0 <= j < i 에 대하여, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]
'''
