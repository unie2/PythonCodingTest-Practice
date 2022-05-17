def solution(s) :
    answer = ''
    for i in range(len(s)) :
        if i == 0 :
            if s[i].isnumeric() :
                answer += s[i]
                continue
            else :
                answer += s[i].upper()
                continue
        if s[i] == ' ' :
            answer += ' '
            continue
        if s[i-1] == ' ' :
            answer += s[i].upper()
        else :
            answer += s[i].lower()

    return answer
  
'''
1. 전달받은 s 문자열의 문자를 하나씩 확인하는데, i가 0일 경우(가장 첫번째 요소를 확인 중이라면) 이와 같은 작업을 수행한다.
  - 해당 문자가 숫자일 경우 answer에 그대로 이어붙이고 continue 한다.
  - 해당 문자가 숫자가 아닐 경우 대문자로 변환한 문자를 answer에 이어붙이고 continue 한다.

2. 현재 확인하고 있는 문자가 공백일 경우 단순히 answer에 공백을 이어붙이고 continue 한다.

3. 현재 확인하고 있는 문자의 이전 문자가 공백이었을 경우 단어의 시작이므로 현재의 문자를 대문자로 변환하여 answer에 이어붙인다.

4. 이전 문자가 공백이 아닐 경우 현재의 문자를 소문자로 변환하여 answer에 이어붙인다.

'''
