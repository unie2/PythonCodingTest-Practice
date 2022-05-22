def solution(n, t, m, p) :
    answer = ''
    str_value = ''

    data = dict()

    for i in range(10) :
        data[i] = str(i)

    data[10] = 'A'
    data[11] = 'B'
    data[12] = 'C'
    data[13] = 'D'
    data[14] = 'E'
    data[15] = 'F'

    for i in range(t * m) :
        temp = ""
        if i == 0 :
            str_value = '0'
            continue

        while i > 0 :
            temp = data[i % n] + temp
            i //= n

        str_value += temp

    for i in range(p-1, t * m, m) :
        answer += str_value[i]

    return answer
  
'''
1. 딕셔너리 data에 0~9까지를 0~9까지로 정의하고, 추가로 10~15까지는 각 'A' ~ 'F' 로 정의한다.
2. 반복문을 통해 진법 변환을 수행하는데, i가 0일 경우 str_value에 '0'을 할당한 후 continue한다.
3. i 값이 0보다 작거나 같을 때까지 진법 변환을 수행한다. while문이 끝나면 정의된 temp 문자열을 str_value에 추가한다.
4. 이와 같은 반복문을 수행한 후 p가 말해야하는 숫자를 answer에 이어붙이고, 최종적으로 정의된 answer를 반환한다.

'''
