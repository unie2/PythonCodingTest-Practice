t = int(input())

for tc in range(1, t + 1) :
    data = input()
    result = ""

    for i in range(len(data) - 1, -1, -1) :
        if data[i] == 'b' :
            result += 'd'
        elif data[i] == 'd' :
            result += 'b'
        elif data[i] == 'p' :
            result += 'q'
        else :
            result += 'p'

    print('#%d %s' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력받은 문자열(data)을 거꾸로 확인하고, 거울에 비추어 표현되는 문자를 result 문자열에 추가한다.
2. 모든 문자에 대한 작업을 마치면 최종적으로 해당 테스트 케이스 번호와 함께 result 문자열을 출력한다.

'''
