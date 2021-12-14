def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1) :
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        
        #단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step) :
            #이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step] :
                count += 1
            # 다른 문자열이 나왔다면
            else :
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
                
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    
    return answer
  
  
# 1. 먼저 전달받은 매개변수 문자열 s의 길이를 구하여 answer에 할당한다.
# 2. 반복문을 통해 1개 단위부터 압축 단위를 늘려가며 문자열을 확인한다.
# 3. 그 과정에서 0번째부터 step만큼의 문자열을 추출하고, step 크기만큼 증가시키며 이전 문자열과 비교한다.
# 4. 이전 문자열과 동일하다면 count를 1 증가시키고, 다르다면 prev와 count의 상태를 다시 초기화한다.
# 5. 내부 반복문이 종료되면 남아 있는 문자열에 대하여 처리하고 min( )를 통해 answer과 compressed길이를 비교하여 더 작은 값을 answer에 갱신한다.
# 6. 반복문이 모두 끝나면 answer 값을 반환한다.
