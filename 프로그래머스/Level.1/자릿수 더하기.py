def solution(n) :
    answer = 0
    n = str(n)
    for value in n :
        answer += int(value)

    return answer
  
# 1. 전달받은 정수형 n을 문자열 형태로 변환하고, 각 자릿수를 정수형으로 변환하여 answer에 더한다.
