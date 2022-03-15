def solution(s):
    listed = s.split(" ")
    
    for i in range(len(listed)) :
        data_list = list(listed[i])
        
        for j in range(len(data_list)) :
            if j % 2 == 0 :
                data_list[j] = data_list[j].upper()
            else :
                data_list[j] = data_list[j].lower()
        listed[i] = ''.join(data_list)
    
    answer = ' '.join(listed)
    return answer
  
'''
1. 전달받은 문자열 s를 공백으로 구분하여 리스트 형태로 구성하여 listed를 정의한다.
2. 이중 for문을 통해 각 단어의 인덱스가 짝수일 경우 대문자 알파벳으로 갱신하고, 홀수일 경우 소문자 알파벳으로 갱신한다.
3. 하나의 단어의 갱신작업이 종료되면 join()을 통해 문자를 합치고, 기존의 listed 요소에 갱신시켜준다.
4. 모든 단어의 반복작업이 끝나면 최종적으로 listed 리스트를 공백으로 구분하여 문자열을 합치고 반환한다.

'''
