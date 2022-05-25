def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)) :
        if participant[i] != completion[i] :
            return participant[i]

    return participant[-1]
  
'''
1. participant 리스트와 completion 리스트를 오름차순으로 정렬한다.
2. for문을 통해 같은 인덱스를 갖는 participant의 문자열과 completion 문자열을 확인하여 두 문자열이 다를 경우 participant[i]를 반환한다.
3. 반복문 내에서 반환된 값이 없다면, participant 리스트의 가장 마지막 문자열을 반환한다.


'''
