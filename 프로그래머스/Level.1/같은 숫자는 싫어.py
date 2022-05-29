def solution(arr) :
    answer = [arr[0]]
    for i in range(1, len(arr)) :
        if arr[i] == answer[-1] :
            continue
        else :
            answer.append(arr[i])

    return answer
  
'''
1. answer 리스트에 arr 리스트의 가장 첫 요소를 할당하여 초기화한다.
2. 반복문을 통해 arr 리스트의 1번째 요소부터 값을 확인하는데, 만약 현재 확인하고 있는 값이 answer 리스트의 가장 마지막 요소와 같다면 continue 한다.
3. 그렇지 않다면 해당 값을 answer 리스트에 추가한다.

'''
