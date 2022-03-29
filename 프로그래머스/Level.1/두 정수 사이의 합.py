def solution(a, b):
    answer = 0
    if a <= b :
        for i in range(a, b + 1) :
            answer += i
    else :
        for i in range(a, b-1, -1) :
            answer += i
    return answer
  
'''
1. 전달받은 a가 b보다 작거나 같을 경우 a부터 b+1까지를 범위로 지정한 반복문을 통해 answer에 값을 하나씩 증가시켜 누적한다.
2. 전달받은 a가 b보다 클 경우 a부터 b-1까지를 범위로 지정한 반복문을 통해 answer에 값을 하나씩 감소시켜 누적한다.

'''
