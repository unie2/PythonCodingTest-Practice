def solution(skill, skill_trees) :
    answer = 0
    for value in skill_trees :
        data = list(skill)
        for info in value :
            if info in data :
                if data.pop(0) != info :
                    break
        else : # for문이 중간에 끊기지 않았다면
            answer += 1

    return answer
  
'''
1. skill_trees의 요소(value)를 하나씩 확인하고, skill 문자열을 리스트 형태로 변환하여 data에 할당한다.
2. value에서 문자를 하나씩 확인하는데, 만약 해당 문자가 data에 존재하고 data에 존재하는 가장 앞에서 빼낸 문자와 다르다면 break한다.
3. 만약 for문이 break 되지 않고 끝까지 수행되었다면 answer을 1 증가시킨다.
4. skill_trees의 요소들을 모두 확인한 후 최종적으로 answer 값을 반환한다.

'''
