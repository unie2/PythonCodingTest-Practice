def solution(s) :
    answer = 0
    temp = [i for i in s]

    for i in range(len(temp)) :
        temp.append(temp.pop(0))
        left = []
        cnt = len(temp)

        for j in temp :
            cnt -= 1
            if j == "[" or j == "(" or j == "{" : # 여는 괄호를 left에 삽입
                left.append(j)
            elif j == "}" : # 닫는 괄호일 경우 left에서 꺼내 확인
                if len(left) == 0 or left.pop() != "{" :
                    cnt = 10
                    break
            elif j == "]" :
                if len(left) == 0 or left.pop() != "[" :
                    cnt = 10
                    break
            elif j == ")" :
                if len(left) == 0 or left.pop() != "(" :
                    cnt = 10
                    break

        if cnt == 0 and len(left) == 0 :
            answer += 1

    return answer
  
'''
1. 전달받은 s문자열에 담긴 문자를 나눠 temp 리스트에 정의한다.
2. temp 리스트의 길이만큼 왼쪽으로 회전하고 temp 리스트의 길이를 cnt에 할당한다.
3. temp 리스트의 각 문자를 하나씩 확인하여 cnt를 1씩 감소하고, 확인하는 문자가 여는 괄호일 경우 left 리스트에 해당 문자를 추가한다.
4. 여는 괄호가 아니고 닫는 괄호일 경우 left 리스트에서 문자를 꺼내고, 만약 꺼낸 문자가 닫는 괄호에 대응하는 여는 괄호가 아닐 경우 cnt를 10으로 갱신하고 break한다.
5. 회전 한 번에 대한 모든 문자 확인이 끝난 후 cnt 값이 0이거 left 리스트의 길이가 0일 경우 answer 값을 1 증가시킨다.

'''
