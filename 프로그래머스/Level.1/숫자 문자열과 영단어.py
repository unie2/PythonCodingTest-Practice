def solution(s):
    answer = ""
    info = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    value = ""
    for i in range(len(s)) :
        if s[i] in '0123456789' :
            answer += s[i]
        else :
            value += s[i]
            if value in info.keys() :
                answer += info[value]
                value = ""
                
    return int(answer)
  
'''
1. 영단어를 숫자로 값을 넣어주기 위해 info 딕셔너리를 정의한다.
2. 전달받은 문자열 s의 문자를 하나씩 확인하여 해당 값이 숫자일 경우 그대로 answer에 추가한다.
3. 문자일 경우 임시 변수 value에 해당 문자열을 추가하고, value가 info 딕셔너리 key값으로 존재할 경우 그에 맞는 숫자를 answer에 추가한 후 value를 빈 문자열로 다시 초기화한다.
4. 반복문이 종료되면 문자열 형태로 이루어진 answer 값을 정수형으로 변환하여 반환한다.

'''
