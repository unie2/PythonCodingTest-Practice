def solution(s) :
    answer = ''
    s = list(map(int, s.split()))
    answer += str(min(s)) + " "
    answer += str(max(s))

    return answer
  
'''
1. 전달받은 s 문자열을 공백으로 기준으로 하여 리스트 형태로 변환한다.
2. s 리스트에서 최솟값을 문자형으로 변환하여 answer에 이어붙이고 공백을 이어붙인다.
3. s 리스트에서 최댓값을 문자형으로 변환하여 answer에 이어붙인 후 최종적으로 answer 문자열을 반환한다.

'''
