def solution(n) :
    temp = set(range(2, n + 1))
    for i in range(2, n + 1) :
        if i in temp :
            temp -= set(range(2 * i, n + 1, i))

    return len(temp)
  
'''
1. 2부터 n까지 수를 삽입한 temp를 정의한다.
2. 2의 배수부터 i의 배수까지 temp 리스트에서 제거한다.
3. 최종적으로 temp 리스트의 길이를 반환한다.

'''
