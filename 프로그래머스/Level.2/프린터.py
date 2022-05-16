def solution(priorities, location) :

    for i in range(len(priorities)) :
        priorities[i] = (i, priorities[i]) # 번호, 중요도

    cnt = 0
    while True :
        value = priorities.pop(0)
        flag = True
        for i in range(len(priorities)) :
            if value[1] < priorities[i][1] :
                priorities.append(value)
                flag = False
                break

        if flag == True :
            cnt += 1
            if value[0] == location :
                return cnt
              
'''
1. 전달받은 priorities의 각 요소에 번호를 포함시켜 (번호, 중요도) 형태로 값을 갱신한다.

2. while문을 통해 아래와 같은 작업을 반복 수행한다.
  - priorities 리스트의 가장 앞에 있는 요소를 꺼내 value에 할당한다.
  - 남아있는 priorities의 요소들과 하나씩 비교하여 value의 중요도가 더 작다면 다시 value를 priorities 리스트에 추가한 후 flag를 False로 갱신한 후 break한다.
  - 반복문이 끝나면 flag 값을 확인하여 그 값이 True일 경우 cnt를 1 증가시키고, value의 0번째 요소(번호)와 location이 같을 경우 cnt를 반환한다.

'''
