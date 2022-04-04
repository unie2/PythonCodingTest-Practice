def solution(numbers, hand):
    answer = ''
    left_present = 10
    right_present = 12
    
    for i in numbers :
        if i in [1, 4, 7] :
            left_present = i
            answer += 'L'
        elif i in [3, 6, 9] :
            right_present = i
            answer += 'R'
        else :
            if i == 0 :
                i = 11
            absLeft = abs(i - left_present)
            absRight = abs(i - right_present)
            
            if sum(divmod(absLeft, 3)) < sum(divmod(absRight, 3)) :
                left_present = i
                answer += 'L'
            elif sum(divmod(absRight, 3)) < sum(divmod(absLeft, 3)) :
                right_present = i
                answer += 'R'
            else :
                if hand == 'left' :
                    left_present = i
                    answer += 'L'
                else :
                    right_present = i
                    answer += 'R'
                    
    return answer
  
'''
1. 초기 왼손 엄지손가락 위치(left_present)와 오른손 엄지손가락 위치(right_present)에 각각 10('*')과 12('#')를 할당한다.
2. 반복문을 통해 전달받은 numbers의 값을 하나씩 확인하여 그 값이 1, 4, 7 중 하나 일 경우 left_present에 그 값을 넣어주고 answer에 'L'을 추가한다.
3. 확인한 값이 3, 6, 9 중 하나일 경우 right_present에 그 값을 넣어주고 answer에 'R'을 추가한다.
4. 모두 해당되지 않을 경우 먼저 그 값이 0인지 확인하고, 0 이라면 11로 갱신한다.
5. 확인하고 있는 값에서 left_present를 뺀 절대값과 right_present를 뺀 절대값을 각각 구해 어느 엄지손가락이 더 가까운지 거리를 구할 수 있도록 초기 세팅을 한다.
6. 각각의 절대값에 대하여 3으로 나눈 몫과 나머지 값을 더한 값을 비교하여 더 작은 값에 대하여 i 값으로 갱신하고 answer에 조건에 맞는 문자를 추가한다.
7. 두 거리가 같을 경우에는 전달받은 hand 문자열을 확인하여 각 조건에 맞도록 i 값으로 갱신하고 answer에 문자를 추가한다.

'''
