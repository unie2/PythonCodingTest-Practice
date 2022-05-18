def solution(s) :
    stack = []

    for value in s :
        if not stack :
            stack.append(value)
        else :
            if stack[-1] == value :
                stack.pop()
            else :
                stack.append(value)

    if stack :
        return 0

    return 1
  
'''
1. 문자열 s의 각 문자를 하나씩 확인하여 stack 리스트에 해당 문자가 없다면 stack 리스트에 해당 문자를 추가한다.
2. 현재 확인하고 있는 문자가 stack 리스트에 있다면 stack 리스트의 가장 마지막 요소와 비교하여 일치하면 마지막 요소를 제거하고, 일치하지 않다면 문자를 리스트에 추가한다.
3. 모든 문자에 대한 확인이 끝나면 최종적으로 stack 리스트를 확인하여 요소가 있다면 0을 반환하고, 아니라면 1을 반환한다.

'''
