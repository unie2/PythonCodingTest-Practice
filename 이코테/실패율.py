def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, N + 1) :
        count = stages.count(i)
        
        if length == 0 :
            fail = 0
        else :
            fail = count / length
            
        answer.append((i, fail))
        length -= count
        
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    
    answer = [i[0] for i in answer]
    return answer
  
  
  # 1. 스테이지 번호를 1부터 N까지 증가시키며 확인하고, 해당 스테이지에 머물러 있는 사람 수를 구하여 count에 할당한다.
  # 2. 조건문을 통해 stages의 길이(length)가 0일 경우 fail에 0을 할당하고, 그렇지 않을 경우에는 문제에서 제시한 실패율을 계산하여 fail에 할당한다.
  # 3. answer 리스트에 현재의 스테이지 번호와 실패율을 원소로 구성하여 삽입하고 length에서 count 값만큼 빼준다.
  # 4. 실패율을 기준으로 각 스테이지를 내림차순으로 정렬한다.
  # 5. 최종적으로 정렬된 스테이지 번호를 반환한다.
