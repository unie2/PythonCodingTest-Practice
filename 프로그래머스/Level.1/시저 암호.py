def solution(s, n):
    answer = ''
    for i in range(len(s)) :
        if ord(s[i]) >= 65 and ord(s[i]) <= 90 :
            value = ord(s[i]) + n
            if value > 90 :
                value = 64 + (value % 90)
                answer += chr(value)
            else :
                answer += chr(ord(s[i]) + n)
        elif ord(s[i]) >= 97 and ord(s[i]) <= 122 :
            value = ord(s[i]) + n
            if value > 122 :
                value = 96 + (value % 122)
                answer += chr(value)
            else :
                answer += chr(ord(s[i]) + n)
        else :
            answer += s[i]

    return answer
  
  
'''
1. 반복문을 통해 전달받은 문자열 s의 각 문자를 하나씩 확인하고, 그 문자가 대문자인지 소문자인지 판별한다.
   (대문자 아스키코드 범위 : 65-90 // 소문자 아스키코드 범위 : 97-122)
2. 대문자, 소문자 판별 후 해당 상황에서 현재 확인하고 있는 문자를 아스키코드 값으로 변환한 후 n을 더하여 value에 할당한다.
3. 조건문을 통해 value의 값이 'Z' 혹은 'z'의 아스키코드 값보다 클 경우 'A' 혹은 'a'의 아스키코드 값에 (value%90)를 더하여 갱신하고, 문자열 answer에 추가한다.
4. 만약 value의 값이 'Z' 혹은 'z' 보다 크지 않을 경우에는 n을 더하여 문자형으로 변환한 뒤 그대로 answer에 추가한다.
5. 반복문 내부에서 현재 확인하고 있는 값이 대문자 알파벳, 소문자 알파벳이 아닌 경우 공백으로 판단하여 answer에 그대로 추가한다.
6. 반복문의 모든 작업이 종료되면 문자열 answer를 반환한다.

'''
