def solution(a, b):
    answer = 0
    for i in range(len(a)) :
        answer += a[i] * b[i]

    return answer
  
# 1. 반복문을 통해 같은 인덱스를 갖는 a 리스트와 b 리스트를 확인하여 두 값을 곱한 뒤 answer에 누적한다.
