def solution(citations) :
    answer = 0
    for count in range(1, len(citations) + 1) :
        up, down = 0, 0
        for i in range(len(citations)) :
            if citations[i] >= count :
                up += 1
            else :
                down += 1

        if up >= count and down <= count :
            if answer < count :
                answer = count

    return answer
  
'''
1. count를 1부터 citations 길이까지 1씩 증가시키면서 반복문을 수행한다.
2. 만약 현재 확인하고 있는 citations의 요소가 count 이상일 경우 up을 1 증가시키고 그렇지 않을 경우 down을 1 증가시킨다.
3. 만약 up 값이 count 이상이고 down 값이 count 이하일 경우 answer와 count 값을 비교하여 더 큰 값을 answer에 갱신한다.
4. 반복 작업이 모두 끝나면 최종적으로 answer 값을 반환한다.

'''
