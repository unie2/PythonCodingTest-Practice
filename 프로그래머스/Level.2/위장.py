def solution(clothes) :
    answer = 1
    info = {}
    for cloth in clothes :
        cloth_type = cloth[1]
        if cloth_type in info :
            info[cloth_type] += 1
        else :
            info[cloth_type] = 2

    for value in info.values() :
        answer *= value

    return answer - 1
  
'''
1. info 딕셔너리에 각 의상의 종류를 key로 설정하여 개수를 증가시킨다.

2. info 딕셔너리에 존재하는 values 값을 가져와 answer에 곱하고, 작업을 마치면 최종적으로 answer-1 값을 반환한다.
   이는 모든 종류의 의상을 아무 것도 입지 않은 경우를 빼준 것을 의미한다.

'''
