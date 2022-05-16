def solution(s) :
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)

    for i in s :
        data = i.split(",")
        for value in data :
            if int(value) not in answer :
                answer.append(int(value))

    return answer
  
'''
1. 전달받은 s 문자열에서 앞에 있는 두 요소( {{ )와 뒤에 있는 두 요소( }} )를 잘라내고, '},{' 문자로 구분하여 s를 갱신한다.
2. s 내에 있는 문자열의 길이를 기준으로 오름차순으로 정렬한다.
3. 문자열을 하나씩 꺼내 ',' 로 구분하여 data에 할당한다.
4. 구분된 data 내 요소를 하나씩 꺼내 해당 문자를 정수형으로 변환한 값이 answer 리스트에 존재하지 않을 경우 해당 수를 answer 리스트에 추가한다.
5. s 내에 존재하는 모든 문자열에 대한 처리 작업이 끝나면 최종적으로 answer 리스트를 반환한다.

'''
