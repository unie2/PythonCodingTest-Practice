from collections import defaultdict

for tc in range(1, 11) :
    n = int(input())
    data = list(input())
    info = defaultdict(int)

    for d in data :
        info[d] += 1

    result = 1
    for k, v in info.items() :
        if k == '(' :
            if info[')'] != v :
                result = 0
                break
        elif k == '[' :
            if info[']'] != v :
                result = 0
                break
        elif k == '{' :
            if info['}'] != v :
                result = 0
                break
        elif k == '<' :
            if info['>'] != v :
                result = 0
                break

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력받은 괄호 문자의 등장 횟수를 info 딕셔너리에 담는다.

2. result를 1로 초기화하고, 반복문을 통해 info 딕셔너리의 요소를 하나씩 가져와 아래와 같은 작업을 수행한다.
  - 만약 키 값(k)이 '('이고 value 값(v)이 ')'의 등장 횟수와 다르다면 result를 0으로 갱신하고 break한다.
  - 만약 키 값(k)이 '['이고 value 값(v)이 ']'의 등장 횟수와 다르다면 result를 0으로 갱신하고 break한다.
  - 만약 키 값(k)이 '{'이고 value 값(v)이 '}'의 등장 횟수와 다르다면 result를 0으로 갱신하고 break한다.
  - 만약 키 값(k)이 '<'이고 value 값(v)이 '>'의 등장 횟수와 다르다면 result를 0으로 갱신하고 break한다.

3. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
