from collections import defaultdict

t = int(input())

for tc in range(1, t + 1) :
    data = input()
    info = defaultdict(int)

    for value in data :
        info[value] += 1

    if len(info) != 2 :
        print('#%d %s' % (tc, 'No'))
    else :
        flag = True
        for v in info.values() :
            if v != 2 :
                flag = False
                break
        if flag :
            print('#%d %s' % (tc, 'Yes'))
        else :
            print('#%d %s' % (tc, 'No'))
            
'''
1. 각 테스트 케이스마다 입력받은 문자열(data)의 문자(value)를 하나씩 확인하여 info 딕셔너리에 해당 알파벳에 대한 등장 횟수를 증가시킨다.
2. 만약 info의 길이가 2가 아닐 경우 해당 테스트 케이스 번호와 함께 'No'를 출력한다.
3. 그렇지 않다면, info 딕셔너리의 value 값을 하나씩 가져와 해당 값이 모두 2일 경우 'Yes'를, 하나라도 2가 아닐 경우 'No'를 출력한다.

'''
