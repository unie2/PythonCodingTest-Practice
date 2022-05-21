def solution(s) :
    left = []

    open = s.count('(')
    close = s.count(')')
    if open != close :
        return False

    for i in range(len(s)) :
        if s[i] == '(' :
            left.append('(')
        else :
            if len(left) == 0 :
                return False
            else :
                left.pop()

    return True
  
  
'''
1. 여는 괄호의 개수(open)와 닫는 괄호의 개수(close) 가 같지 않다면 올바르지 않은 괄호 형식이므로 False를 반환한다.
2. 1번에서 False가 반환되지 않았다면, 괄호 문자를 하나씩 확인하고, 해당 문자가 여는 괄호라면 left 리스트에 해당 문자를 추가한다.
3. 만약 현재 확인하고 있는 문자가 닫는 괄호일 경우 left 리스트 길이를 확인하고, 길이가 0이라면 False를 반환한다.
4. left 리스트의 길이가 0이 아니라면 문자를 하나 제거한다.
5. 모든 반복 작업을 마쳤음에도 False가 반환되지 않았다면 최종적으로 True를 반환한다.

'''
