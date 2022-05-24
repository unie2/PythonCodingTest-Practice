def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)) :
        if signs[i] == True :
            answer += absolutes[i]
        else :
            answer += (-absolutes[i])

    return answer
  
'''
1. 반복문을 통해 signs의 값을 하나씩 확인하는데, 현재 확인하고 있는 signs의 값이 True라면 absolutes[i]의 값 그대로 answer에 누적한다.
2. 만약 signs[i]의 값이 False라면 absolutes[i]의 값을 음수로 만들어 answer에 누적한다.

'''
