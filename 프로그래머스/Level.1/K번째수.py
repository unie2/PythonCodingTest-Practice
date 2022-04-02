def solution(array, commands):
    answer = []
    for i in range(len(commands)) :
        arr = array[commands[i][0]-1:commands[i][1]]
        arr.sort()
        answer.append(arr[commands[i][2]-1])
    
    return answer
  
'''
1. 전달받은 commands의 길이만큼 반복 작업하는데, 각 0번째 요소와 1번째 요소를 통해 array리스트 요소를 잘라 arr에 할당한다.
2. arr 리스트를 오름차순으로 정렬하고 2번째 요소-1 에 있는 수를 answer에 추가한다.
3. 반복문이 종료되면 answer를 반환한다.

'''
