for tc in range(int(input())) :
    data = list(input())
    result = ''
    if data == data[::-1] :
        result = 'Exist'
    else :
        for i in range(len(data)) :
            if data[i] == '?' :
                data[i] = data[len(data) - (i + 1)]
            if data == data[::-1] :
                result = 'Exist'
            else :
                result = 'Not exist'

    print('#%d %s' % (tc + 1, result))
    
'''
1. 각 테스트 케이스마다 입력받은 data 문자열과 뒤집은 문자열이 같다면 result에 'Exist' 문자열을 할당한다.
2. 두 문자열이 다르다면 data 문자열의 문자를 하나씩 확인하고, 해당 문자가 '?' 일 경우 data[len(data) - (i + 1)] 문자를 해당 인덱스에 할당한다.
3. 이후 만약 현재의 data 문자열과 뒤집은 문자열이 같다면 result에 'Exist' 문자열을 할당하고, 다르다면 'Not exist' 문자열을 할당한다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 result 문자열을 출력한다.

'''
