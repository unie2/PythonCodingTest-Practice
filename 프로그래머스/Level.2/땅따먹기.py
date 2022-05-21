def solution(land):
    dp = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    for i in range(len(land)) :
        for j in range(4) :
            if i == 0 :
                dp[i][j] = land[i][j]
                continue
            else :
                for k in range(4) :
                    if j == k :
                        continue
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + land[i][j])
    answer = max(dp[-1])
    return answer
  
  
'''
1. 각 인덱스 별로 최댓값을 담을 dp 2차원 리스트를 정의한다.

2. 이중 for문을 통해 최대값을 갱신해 나아가는데, 작업은 아래와 같다.
  - 만약 i가 0일 경우 가장 처음 행을 확인하는 것이므로 dp[i][j]에 land[i][j] 값을 할당한다.
  - i가 0이 아닐 경우 각 열을 확인하고, j와 k가 같다면 바로 윗행의 같은 열에 해당하므로 continue 한다.
  - j와 k 값이 다르다면 dp[i][j]에 현재의 dp[i][j] 값과 이전 행의 k열 값 + 현재 위치의 land 값을 비교하여 더 큰 값을 할당한다.

3. 위 반복 수행을 모두 마치면 dp 리스트에 존재하는 마지막 행에서 가장 큰 값을 answer에 할당하여 반환한다.

'''
