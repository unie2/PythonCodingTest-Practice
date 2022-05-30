def solution(msg) :
    answer = []
    info = {}
    for i in range(26) :
        info[chr(65+i)] = i + 1

    next_info_num = 27
    index = 0
    i = 1

    while True :
        while msg[index:index + i] in info :
            i += 1
            if index + i - 1 > len(msg) :
                break
        answer.append(info[msg[index:index+i-1]])
        if index + i -1 > len(msg) :
            break
        if msg[index:index+i] not in info :
            info[msg[index:index+i]] = next_info_num
            next_info_num += 1
            index += i - 1
            i = 1
    return answer
  
'''
1. 'A': 1, 'B': 2, 'C': 3, ...., 'Z': 26 와 같은 형태로 info 딕셔너리를 정의한다.

2. while문을 통해 info에 없는 문자열이 등장할 때까지 확인하고, 이전 문자열까지의 info 값을 answer에 할당한다.

3. 만약 현재 index + i -1 값이 msg의 길이보다 클 경우 break한다.

4. info에 없는 문자열을 키로, next_info_num을 값으로 info 딕셔너리에 넣어주고 next_info_num을 1 증가시켜준다.
   또한, index에 i-1을 더해주고 다음 확인 작업을 위해 i를 1로 다시 초기화한다.

5. 위 반복 수행 작업에서 갱신된 answer 리스트를 반환한다.

'''
