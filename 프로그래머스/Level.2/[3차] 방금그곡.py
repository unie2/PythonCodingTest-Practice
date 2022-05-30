def replacement(data) :
    data = data.replace('C#', 'c')
    data = data.replace('D#', 'd')
    data = data.replace('F#', 'f')
    data = data.replace('G#', 'g')
    data = data.replace('A#', 'a')

    return data

def solution(m, musicinfos) :
    answer = ''
    m = replacement(m)

    max_time = 0
    for music in musicinfos :
        start, end, name, info = music.split(",")
        info = replacement(info)

        play_time = (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:]))
        index = 0
        value = ''
        time = play_time
        while time :
            value += info[index]
            if index + 1 == len(info) :
                index = -1
            index += 1
            time -= 1

        if m in value :
            if answer :
                if max_time >= play_time :
                    continue
            max_time = play_time
            answer = name

    if answer :
        return answer
    else :
        return '(None)'
      
'''
1. 'C#', 'D#', 'F#', 'G#', 'A#'을 각 'c', 'd', 'f', 'g', 'a'로 치환하는 replacement() 함수를 정의한다.
2. 전달받은 문자열 m을 replacement() 함수에 전달하여 치환 작업을 수행한다.
3. musicinfos의 요소(music)를 꺼내 각 시작 시간(start), 끝 시간(end), 곡 이름(name), 곡 정보(info)를 할당한다.
4. info는 replacement() 함수에 전달하여 치환 작업을 수행한다.
5. 시작 시간(start)과 끝 시간(end)의 차이를 분 단위로 하여 play_time에 할당한다.
6. time이 0이 될 때까지 while문을 수행하며, value문자열에 info[index]를 이어붙이고, 만약 index+1이 info 문자열의 길이와 같다면 다시 처음 정보부터 시작해야하므로 index를 -1로 갱신한다.
7. index를 1 증가시키고 time은 1 감소시킨다.
8. while문 작업이 끝난 후 m이 value에 존재하고 answer에 값이 이미 존재하고 max_time이 play_time보다 크거나 같다면 continue한다.
9. m이 value에 존재하고 answer에 값이 없다면 max_time을 play_time으로 갱신하고 answer에 name을 할당한다.
10. music을 모두 확인하면 최종적으로 answer 값을 확인하고, 만약 answer에 값이 존재한다면 answer을 반환하고, 그렇지 않다면 '(None)'을 반환한다.

'''
