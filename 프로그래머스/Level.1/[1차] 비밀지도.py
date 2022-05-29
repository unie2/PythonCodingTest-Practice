def solution(n, arr1, arr2) :
    answer = []
    temp1 = []
    temp2 = []
    for value in arr1 :
        value = bin(value)[2:]
        value = '0' * (n - len(value)) + value
        temp1.append(value)

    for value in arr2 :
        value = bin(value)[2:]
        value = '0' * (n - len(value)) + value
        temp2.append(value)

    for i in range(n) :
        value = ""
        for j in range(n) :
            if temp1[i][j] == '0' and temp2[i][j] == '0' :
                value += " "
            else :
                value += "#"
        answer.append(value)

    return answer
  
'''
1. 전달받은 arr1리스트와 arr2 리스트의 요소를 각각 가져와 2진수 형태로 변환하고, n개의 길이를 채우기 위해 앞에 '0'을 채워 각각 temp1 리스트와 temp2 리스트에 추가한다.
2. temp1 리스트와 temp2 리스트의 각 위치를 확인하여 두 값이 모두 '0'일 경우 두 지도 모두 공백이므로 value에 공백을 추가한다.
3. 지도 하나라도 해당 위치가 벽일 경우 value에 "#"를 추가한다.
4. 하나의 열에 대한 확인 작업이 끝나면 answer 리스트에 value를 추가한다.
5. 모든 행에 대한 확인 작업이 끝나면 최종적으로 answer 리스트를 반환한다.

'''
