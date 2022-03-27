def solution(s):
    answer = sorted(s, reverse=True)
    answer = "".join(answer)
    return answer
  
'''
1. sorted()를 사용하여 s를 정렬하고, reverse=True를 통해 내림차순으로 정렬한다.
2. 1번의 작업을 하면 answer은 리스트 형태로 구성되므로, join()을 통해 문자열 형태로 변환하여 반환한다.

'''
