t = int(input())

for tc in range(1, t + 1) :
    a, b = input().split()
    dp = [[0] * (len(a) + 1) for _ in range(len(b) + 1)]

    for i in range(1, len(dp)) :
        for j in range(1, len(dp[i])) :
            # 같을 경우
            if a[j-1] == b[i-1] :
                dp[i][j] = dp[i-1][j-1] + 1
            else : # 다를 경우
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print('#%d %d' % (tc, dp[-1][-1]))
    
'''
1. 각 테스트 케이스마다 입력받은 a, b의 길이를 통해 2차원 리스트 dp를 정의한다.
2. 문자를 하나씩 확인하며, 만약 a[j-1]와 b[i-1]이 같을 경우 dp[i][j] 위치에 dp[i-1][j-1] 에 1을 더한 값을 할당한다.
3. 다를 경우 dp[i-1][j]와 dp[i][j-1] 값 중 최댓 값을 dp[i][j]에 할당한다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 dp 리스트의 마지막 행의 마지막 열에 존재하는 값을 출력한다.

'''
