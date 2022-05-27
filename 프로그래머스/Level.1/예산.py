def solution(d, budget) :
    d.sort()
    temp_sum = 0
    answer = 0
    for i in range(len(d)) :
        if temp_sum + d[i] > budget :
            break
        temp_sum += d[i]
        answer += 1

    return answer
  
'''
1. 최대한 많은 부서에 지원해주기 위해 전달받은 d 리스트를 오름차순으로 정렬한다.
2. temp_sum에 각 부서의 필요 예산(d[i])을 더했을 때 budget보다 커진다면 break한다.
3. break 되지 않았다면 temp_sum에 각 부서의 필요 예산을 더하고 answer을 1 증가시킨다.
4. 반복문이 종료되면 최종적으로 answer 값을 반환한다.

'''
