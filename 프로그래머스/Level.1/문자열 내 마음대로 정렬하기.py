def solution(strings, n):
    answer = sorted(strings, key=lambda x : (x[n], x))
    return answer
  
'''
1. 파이썬에서 사용할 수 있는 lambda를 통해 문제를 쉽게 해결할 수 있다.
2. (x[n], x) 에서 첫번째 정렬 기준을 x[n]으로 하고, 만약 x[n] 값이 같다면 문자열 x를 오름차순한다.

'''
