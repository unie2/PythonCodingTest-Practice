def solution(s) :
    s = s.lower()
    count_p = s.count("p")
    count_y = s.count("y")

    if count_p == count_y :
        return True
    else :
        return False
      
'''
1. 전달받은 문자열 s의 요소들을 모두 소문자로 변환한다.
2. s문자열에 존재하는 "p"의 개수를 count_p에 할당하고, "y"의 개수를 count_y에 할당한다.
3. 만약 count_p와 count_y가 같다면 True를 반환하고, 그렇지 않다면 False를 반환한다.

'''
