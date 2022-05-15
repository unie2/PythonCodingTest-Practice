def solution(record) :
    answer = []
    info = {}
    value = []
    for i in range(len(record)) :
        state = list(record[i].split(" "))
        if len(state) >= 3 :
            # Enter 혹은 Change일 경우
            if state[0] == "Enter" :
                info[state[1]] = state[2]
                value.append([state[1], state[0]])
            elif state[0] == "Change" :
                info[state[1]] = state[2]
        else : # Leave일 경우
            value.append([state[1], state[0]])

    for i in range(len(value)) :
        if value[i][1] == "Enter" :
            str_value = "님이 들어왔습니다."
        elif value[i][1] == "Leave" :
            str_value = "님이 나갔습니다."
        answer.append(info[value[i][0]] + str_value)


    return answer
  
'''
1. 각 uid별로 갱신된 닉네임(name)을 담기 위해 info 딕셔너리를 정의한다.

2. 전달받은 record 리스트의 요소를 하나씩 꺼내 공백으로 나눠 리스트 형태로 구성하여 state에 할당한다.

3. state의 길이가 3 이상일 경우 Enter 혹은 Change 명령이 존재하고 이에 대한 처리 작업은 아래와 같다.
  - state의 0번째 요소가 "Enter"일 경우 해당 uid의 닉네임 값을 state[2]로 할당하고, value 리스트에 [uid, 명령] 형태로 추가한다.
  - state의 0번째 요소가 "Change"일 경우 해당 uid의 닉네임 값을 state[2]로 갱신한다.

4. state의 길이가 3 미만일 경우는 Leave 명령에 해당되며, value 리스트에 [uid, 명령] 형태로 추가한다.

5. 위 반복작업을 모두 마치면 value 리스트의 요소를 하나씩 확인하고, 아래와 같이 작업을 수행한다.
  - 현재 확인하고 있는 요소의 첫 번째 값이 "Enter"일 경우 str_value에 "님이 들어왔습니다."를 할당한다.
  - 현재 확인하고 있는 요소의 첫 번째 값이 "Leave"일 경우 str_value에 "님이 나갔습니다."를 할당한다.
  - info 딕셔너리에서 uid에 대한 값(닉네임)을 가져와 str_value 문구를 합쳐 answer 리스트에 할당한다.

6. answer 리스트 구성을 모두 완료하면 최종적으로 answer 리스트를 반환한다.

'''
