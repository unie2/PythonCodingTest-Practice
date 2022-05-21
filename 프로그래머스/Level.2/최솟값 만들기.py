def solution(A, B) :
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)) :
        answer += A[i] * B[i]

    return answer
  
'''
1. 전달받은 A 리스트를 오름차순으로 정렬하고, B 리스트를 내림차순으로 정렬한다.
2. A와 B 리스트의 같은 인덱스에 존재하는 두 값을 곱하여 answer에 누적한다.

'''
