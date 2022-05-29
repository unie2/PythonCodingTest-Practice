def solution(n) :
    n = list(str(n))
    n.sort(reverse=True)
    n = "".join(n)

    return int(n)
  
'''
1. 전달받은 정수 값 n을 문자열 형태로 변환하고 리스트 형태로 갱신한다.
2. n을 내림차순으로 정렬하고 각 요소들을 이어붙인다.
3. 최종적으로 n을 정수형으로 변환하여 반환한다.

'''
