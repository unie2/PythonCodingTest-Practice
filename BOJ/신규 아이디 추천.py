def solution(new_id):
    # 1단계 수행
    new_id = new_id.lower()
    # 2단계 수행
    answer = ''
    for i in new_id :
        if i.isalnum() or i in '-_.' :
            answer += i
    # 3단계 수행
    while '..' in answer :
        answer = answer.replace('..', '.')
    # 4단계 수행
    if answer[0] == '.' and len(answer) > 1 :
        answer = answer[1:]
    if answer[-1] == '.' :
        answer = answer[:-1]
    # 5단계 수행
    if answer == '' :
        answer = 'a'
    # 6단계 수행
    if len(answer) >= 16 :
        answer = answer[:15]
        if answer[-1] == '.' :
            answer = answer[:-1]
    # 7단계 수행
    if len(answer) <= 2 :
        for k in range(3 - len(answer)) :
            answer += answer[-1]
    
    
    return answer
  
'''
1. 1단계 : lower()를 통해 new_id에 존재하는 모든 대문자를 대응되는 소문차로 치환한다.
2. 2단계 : new_id의 문자를 하나씩 확인하여 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 중 하나인 경우에만 answer에 추가한다.
3. 3단계 : 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환한다.
4. 4단계
  - answer의 첫번째 문자가 마침표(.)이고, answer의 길이가 1보다 클 경우 answer의 0번째 요소를 제거한다.
  - answer의 마지막 문자가 마침표(.)일 경우 answer의 마지막 요소를 제거한다.
5. 5단계 : answer가 빈 문자열이라면, answer에 'a'를 대입한다.
6. 6단계
  - answer의 길이가 16자 이상이면 첫 15개의 문제를 제외한 나머지 문자들을 모두 제거한다.
  - answer 갱신 후 마지막 요소가 마침표(.)일 경우 그 값을 제거한다.
7. 7단계 : answer의 길이가 2자 이하라면 마지막 문자를 answer의 길이가 3이 될 때까지 반복해서 끝에 붙인다.

'''
