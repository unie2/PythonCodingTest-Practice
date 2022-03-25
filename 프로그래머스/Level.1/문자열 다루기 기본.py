def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6 :
        answer = False
    else :
        for i in range(len(s)) :
            if ord(s[i]) >= 65 :
                answer = False
                break
    
    return answer
  
'''
1. 가장 먼저 전달받은 s의 길이를 확인하여 그 길이가 4도 아니고 6도 아닐 시 answer을 False로 갱신한다.
2. 문자열의 길이가 4 혹은 6일 경우, 반복문을 통해 문자열의 문자를 하나씩 확인한다.
3. 현재 확인하고 있는 문자를 아스키코드로 변환하여 65이상이라면 (즉, 알파벳이라면) answer을 False로 갱신한다.

'''
