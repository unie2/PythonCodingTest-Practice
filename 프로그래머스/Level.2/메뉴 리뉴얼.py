from itertools import combinations
from collections import Counter

def solution(orders, course) :
    answer = []
    data = []

    for order in orders :
        # 문자열 정렬
        order = sorted(order)
        # 조합
        for c in course :
            data += combinations(order, c)

    # 빈도수로 정렬
    value = Counter(data).most_common()
    
    map_info = {}
    for k, v in value :
        if len(k) not in map_info.keys() or map_info[len(k)] == v :
            if v <= 1 :
                break
            answer.append(''.join(k))
            map_info[len(k)] = v

    answer = sorted(answer)
    return answer
  
'''
1. 전달받은 orders 리스트의 문자열을 하나씩 꺼내 오름차순으로 정렬을 수행한다.
2. course의 요소를 하나씩 확인하여 해당 개수(c)만큼 정렬된 order을 조합하여 data 리스트에 추가한다.
3. 이후 Counter() 를 통해 빈도수로 정렬하여 value에 저장하고 map_info 딕셔너리에 (문자 개수 : 빈도 수) 형태로 할당한다.
   하나의 작업을 수행할 때 map_info에 해당 문자 개수가 존재하지 않거나, 값이 존재한다면 map_info의 값과 v의 값이 동일할 경우에만 작업을 수행한다.
   또한, 문제에서 '최소 2명 이상'의 조건이 있으므로 v가 1 이하라면 break한다.
4. answer 리스트를 오름차순으로 정렬하여 반환한다.

'''
