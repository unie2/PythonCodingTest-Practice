def solution(n):
    answer = ''
    
    for i in range(n) :
        if i % 2 == 0 :
            answer += '수'
        else :
            answer += '박'
            
    return answer
  
'''
1. 반복문을 통해 인덱스를 하나씩 확인하여 해당 인덱스의 값이 짝수일 경우 '수'를, 그렇지 않을 경우 '박'을 answer에 추가한다.
2. 반복문이 종료되면 최종적으로 answer를 반환한다.

'''
