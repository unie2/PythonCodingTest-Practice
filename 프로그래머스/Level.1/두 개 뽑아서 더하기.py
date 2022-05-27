from itertools import combinations

def solution(numbers) :
    answer = []
    for value in combinations(numbers, 2) :
        answer.append(sum(value))

    answer = list(set(answer))
    answer.sort()
    return answer
  
'''
1. itertools.combinations() 모듈을 통해 서로 다른 인덱스에 있는 두 개의 수를 뽑아 두 수의 합을 answer리스트에 추가한다.
2. answer 리스트 내 요소에 존재하는 중복 값을 제거한 후 오름차순으로 정렬하여 반환한다.

'''
