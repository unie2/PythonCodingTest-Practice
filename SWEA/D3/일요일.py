t = int(input())

info = {'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6, 'SUN': 7}
for tc in range(1, t + 1) :
    data = input()
    if data == 'SUN' :
        print('#%d %d' % (tc, 7))
    else :
        print('#%d %d' % (tc, info['SUN'] - info[data]))
        
'''
1. 각 요일 문자열을 key로, 번호를 value로 설정한 info 딕셔너리를 정의한다.
2. 각 테스트 케이스마다 data를 입력받고, 그 값이 'SUN'일 경우 해당 테스트 케이스 번호와 함께 7을 출력한다.
3. 그렇지 않을 경우 info 딕셔너리의 일요일 값(value)에서 입력받은 요일의 값(value)을 빼서 출력한다.

'''
