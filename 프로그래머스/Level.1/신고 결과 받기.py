from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
    report = set(report) # 중복 제거
    count = defaultdict(int) # 신고 횟수
    user = defaultdict(set) # 신고 리스트
    
    for i in report :
        a, b = i.split() # a가 b를 신고
        user[a].add(b)
        count[b] += 1 # 신고 당한 횟수 증가
        
    for id in id_list :
        value = 0
        for j in user[id] :
            if count[j] >= k :
                value += 1
        
        answer.append(value)
        
    return answer
  
'''
1. 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리되므로 report 내 요소의 중복을 제거한다.
2. 신고 당한 횟수를 의미하는 count와 신고 리스트 user 딕셔너리를 정의한다.
3. 반복문을 통해 report의 요소를 하나씩 확인하면서 하나의 요소에서 공백을 기준으로 신고자(a)와 신고당한 자(b)를 구한다.
4. 이후 신고 리스트 user의 a에 대응하여 b를 추가하고, b가 신고 당한 횟수를 1 증가시킨다.
5. 이와 같은 반복 수행이 끝나면 이용자별로 자신이 신고한 사람이 k번 이상이면 처리된 횟수(value)를 1씩 증가시키며, answer에 추가한다.
6. 최종적으로 각 유저별로 처리 결과 메일을 받은 횟수가 담겨 있는 answer 리스트를 반환한다.

'''
