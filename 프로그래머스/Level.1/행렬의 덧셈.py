def solution(arr1, arr2):
    for i in range(len(arr1)) :
        for j in range(len(arr1[0])) :
            arr1[i][j] += arr2[i][j]
    
    return arr1
  
# 1. 두 개의 행렬 arr1과 arr2를 매개변수로 받아, 행렬 덧셈의 결과를 반환한다.
