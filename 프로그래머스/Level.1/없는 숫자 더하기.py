def solution(numbers):
    answer = 0
    for i in range(1, 10) :
        if i not in numbers :
            answer += i
            
    return answer
  
  
# 1. 1부터 9까지 수를 확인하여 각 수가 numbers 리스트에 존재하지 않을 경우 answer에 값을 누적한다.
