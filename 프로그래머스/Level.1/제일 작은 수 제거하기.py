def solution(arr):
    if len(arr) <= 1 :
        return [-1]
    arr.remove(min(arr))
    
    return arr
  
'''
1. 전달받은 arr 리스트의 길이가 1 이하일 경우 문제에서 요구하는 정답을 도출할 수 없으므로 [-1]을 반환한다.
2. 그렇지 않을 경우 remove()를 통해 arr 리스트에서 가장 작은 수를 제거하여 반환한다.

'''
