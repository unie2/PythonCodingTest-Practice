t = int(input())

for tc in range(1, t + 1) :
    data = input()
    reversed_data = data[::-1]
    result = 'Not exist'
    for i in range(len(data)) :
        if data[i] == reversed_data[i] :
            continue
        if data[i] == '*' or reversed_data[i] == '*' :
            result = 'Exist'
            break
        else :
            break
    else :
        result = 'Exist'

    print('#%d %s' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력받은 문자열 data를 뒤집어 reversed_data에 저장한다.
2. 가장 처음 result 값은 'Not exist'로 초기화하고, data문자열과 reversed_data문자열의 문자를 하나씩 확인한다.
3. 만약 두 문자가 같다면 continue한다.
4. 만약 두 문자가 다르지만, 둘 중 하나의 문자가 '*' 일 경우 팰린드롬이 될 수 있으므로 result 값을 'Exist'로 갱신한 후 break 한다.
5. 만약 두 문자가 다르고 '*' 문자도 존재하지 않는다면 break한다.
6. 두 문자열에 '*' 가 없고 모든 문자가 같다면 result 값을 'Exist'로 갱신한다.
7. 최종적으로 해당 테스트 케이스 번호와 함께 result값을 출력한다.

'''
