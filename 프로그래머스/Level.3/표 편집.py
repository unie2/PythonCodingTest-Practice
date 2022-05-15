def solution(n, k, cmd) :
    info = {x: [x-1, x+1] for x in range(n)}
    answer = ['O' for _ in range(n)]
    deleted = []

    for value in cmd :
        if len(value) >= 2 :
            value, count = value.split(" ")
        if value == 'U' : # 위로
            for _ in range(int(count)) :
                k = info[k][0]
        elif value == 'D' : # 아래로
            for _ in range(int(count)) :
                k = info[k][1]
        elif value == 'C' :
            pre, next = info[k]
            deleted.append((pre, next, k))
            answer[k] = 'X'

            if pre == -1 :
                info[next][0] = pre
                k = next
            elif next == n :
                info[pre][1] = next
                k = pre
            else :
                info[pre][1] = next
                info[next][0] = pre
                k = next
        elif value == 'Z' :
            pre, next, now = deleted.pop()
            answer[now] = 'O'
 
            if pre == -1 :
                info[next][0] = now
            elif next == n :
                info[pre][1] = now
            else :
                info[pre][1] = now
                info[next][0] = now

    return "".join(answer)
  
'''
1. 연결 리스트 info를 정의하고, 반환할 answer 리스트와 삭제 정보를 담을 deleted 리스트를 정의한다.
2. value의 값이 'U'일 경우 count 만큼 위로 이동해야하므로 이전 인덱스를 가져와 k를 갱신한다.
3. value의 값이 'D'일 경우 count 만큼 아래로 이동해야하므로 다음 인덱스를 가져와 k를 갱신한다.
4. value의 값이 'C'일 경우 기준 값의 이전 값과 다음 값을 가져와 삭제처리하고 answer[k]의 값을 'X'로 갱신한다.
5. 이후 이전 값이 -1 즉, 가장 상단에 있는 행이 삭제될 경우 다음 기준 값의 이전 값을 -1로 갱신하고, k를 다음 기준 값으로 갱신한다.
6. 다음 값이 n, 즉 가장 하단에 있는 행이 삭제될 경우 이전 기준 값의 다음 값을 n으로 갱신하고, k를 이전 기준 값으로 갱신한다.
7. 중간에 있는 값을 삭제할 경우 이전 기준 값의 다음 값과 다음 기준 값의 이전 값을 갱신하고, k를 다음 기준 값으로 갱신한다.
8. value의 값이 'Z'일 경우 가장 최근에 삭제된 기준 값(기준 값에 대한 이전 값과 다음 값 포함)을 가져온 후 answer[now] 값을 'O'로 갱신한다.
9. 이후 이전 값이 -1일 경우 다음 기준 값의 이전 값을 now로 갱신하여 다시 행에 넣도록 한다.
10. 다음 값이 n일 경우 이전 기준 값의 다음 값을 now로 갱신하여 다시 행에 넣도록 한다.
11. 중간에 삽입할 경우 두 기준 값에 대한 이전 혹은 다음 값을 now로 갱신한다.
12. cmd 작업을 모두 마치면 최종적으로 answer 리스트의 문자를 모두 이어 붙여 문자열 형태로 값을 반환한다.

'''
