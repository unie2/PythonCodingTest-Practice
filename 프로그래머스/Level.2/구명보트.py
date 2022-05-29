from collections import deque

def solution(people, limit) :
    answer = 0
    people.sort()
    people = deque(people)

    while people :
        if len(people) == 1 :
            answer += 1
            break

        if people[0] + people[-1] > limit :
            people.pop()
            answer += 1
        else :
            people.pop()
            people.popleft()
            answer += 1

    return answer
  
'''
1. 전달받은 people 리스트를 오름차순으로 정렬하고 deque() 로 감싸 갱신한다.
2. people 리스트에 존재하는 요소가 1개라면 answer 값을 1 증가시킨 후 break한다.
3. 만약 people 리스트의 가장 첫 요소와 마지막 요소를 더한 값이 limit 보다 클 경우 마지막 요소만 제거한 후 answer을 1 증가시킨다.
4. 더한 값이 limit보다 작거나 같을 경우 두 요소를 제거한 후 answer을 1 증가시킨다.
5. 최종적으로 answer 값을 반환한다.

'''
