def solution(answers):
    answer = [0 for i in range(3)] 
    
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)) :
        if (first[i % len(first)] == answers[i]) :
            answer[0] += 1
        if (second[i % len(second)] == answers[i]) :
            answer[1] += 1
        if (third[i % len(third)] == answers[i]) :
            answer[2] += 1
            
    result = []
    for i in range(3) :
        if answer[i] == max(answer) :
            result.append(i + 1)
    
    return sorted(result)
  
'''
1. 1번~3번 수포자가 찍는 방식을 각 first, second, third 리스트에 할당하여 초기화한다.
2. 전달받은 answers의 길이만큼 반복하여 각 first, second, third의 해당 인덱스 값이 answers[i] 요소와 같을 경우 answer에 해당되는 인덱스 값을 1 증가시킨다.
3. answer 값을 하나씩 확인하여 최대값과 같을 경우 result 리스트에 i + 1을 추가한다.
4. 최종적으로 result를 오름차순으로 정렬하여 반환한다.

'''
