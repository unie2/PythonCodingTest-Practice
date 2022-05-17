def solution(arr1, arr2) :
    row = len(arr1)
    col = len(arr2[0])

    answer = [[0] * col for _ in range(row)]
    for i in range(row) :
        for j in range(col) :
            for k in range(len(arr2)) :
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer
  
'''
1. arr1에 존재하는 하나의 열을 arr2에 존재하는 하나의 행을 곱하여 answer[i][j]에 누적한다.
2. 위와 같이 행렬의 곱셈 작업을 수행을 마친 후 최종적으로 answer를 반환한다.

'''
