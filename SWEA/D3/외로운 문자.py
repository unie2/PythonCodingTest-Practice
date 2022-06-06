from collections import defaultdict

t = int(input())

for tc in range(1, t + 1) :
    data = input()
    info = defaultdict(int)
    result = ""

    for d in data :
        info[d] += 1

    for key in info.keys() :
        info[key] %= 2

    for key, value in info.items() :
        if value > 0 :
            result += key * value

    if result :
        result = sorted(result)
        print('#%d %s' % (tc, ''.join(result)))
    else :
        print('#%d %s' % (tc, 'Good'))
        
'''
1. 각 테스트 케이스마다 문자열(data)을 입력받고 각 문자(d)를 key로 하여 등장 횟수를 info 딕셔너리에 저장한다.
2. info 딕셔너리의 key 값을 가져와 해당 key에 대응하는 value 값을 2로 나눈 나머지 값으로 갱신한다.
3. 이후 info 딕셔너리에서 key, value를 가져와 value 값이 0보다 클 경우에만 해당 갯수만큼의 문자를 result에 이어붙인다.
4. 만약 result에 문자가 존재한다면 오름차순으로 정렬한 후 해당 테스트 케이스 번호와 함께 문자를 이어붙인 result를 출력한다.
5. 그렇지 않을 경우 어떠한 문자도 남지 않았으므로 해당 테스트 케이스 번호와 함께 'Good'을 출력한다.

'''
