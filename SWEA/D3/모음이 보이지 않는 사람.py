t = int(input())

for tc in range(1, t + 1) :
    data = input()
    result = ''
    for i in range(len(data)) :
        if data[i] in ['a', 'e', 'i', 'o', 'u'] :
            continue
        result += data[i]

    print('#%d %s' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력받은 data 문자열의 문자를 하나씩 확인한다.
2. 해당 문자가 모음일 경우 continue하고, 자음일 경우에는 result에 해당 문자를 추가한다.
3. 최종적으로 해당 테스트 케이스 번호와 함께 result 문자열을 출력한다.

'''
