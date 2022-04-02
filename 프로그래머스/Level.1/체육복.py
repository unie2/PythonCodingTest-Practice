def solution(n, lost, reserve):
    lost_update = list(set(lost) - set(reserve))
    reserve_update = list(set(reserve) - set(lost))
    
    answer = n - len(lost_update)
    for i in lost_update :
        if i-1 in reserve_update :
            answer += 1
            reserve_update.remove(i-1)
        elif i+1 in reserve_update :
            answer += 1
            reserve_update.remove(i+1)
            
    return answer
  
'''
1. 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있다고 하였으므로, set을 통해 중복을 제거한다.
2. answer의 초기값은 입력받은 n에서 lost_update의 길이를 뺀 값으로 설정한다.
3. 반복문을 통해 도난당한 학생(lost_update)을 한명씩 확인하고, i-1 값이 reserve_update에 있을 경우 answer를 1 증가시키고 reserve_update에서 i-1을 제거한다.
4. 그렇지 않고 i+1 값이 reserve_update에 있을 경우 answer를 1 증가시키고 reserve_update에서 i+1을 제거한다.
5. 반복문이 종료되면 answer를 반환한다.

'''
