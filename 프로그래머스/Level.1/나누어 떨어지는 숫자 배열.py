def solution(arr, divisor):
    answer = []
    for i in arr :
        if i % divisor == 0 :
            answer.append(i)
    if len(answer) == 0 :
        return [-1]
    else :
        return sorted(answer)
      
'''
1. 반복문을 통해 arr리스트 내 요소들을 하나씩 확인하여 divisor로 나누어 떨어질 경우 answer리스트에 값을 추가한다.
2. 반복문 작업이 끝난 후 answer리스트의 길이가 0일 경우 divisor로 나누어 떨어지는 요소가 하나도 없으므로 [-1]을 반환한다.
3. 그렇지 않을 경우 answer리스트를 정렬하여 반환한다.

'''
