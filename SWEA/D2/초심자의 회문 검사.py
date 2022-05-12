t = int(input())

for tc in range(1, t + 1) :
    data = input()
    temp = ''
    for i in range(len(data)-1, -1, -1) :
        temp += data[i]

    if data == temp :
        print('#%d %d' % (tc, 1))
    else :
        print('#%d %d' % (tc, 0))
        
'''
1. 각 테스트 케이스마다 문자열을 입력받아 각 알파벳을 거꾸로 하여 temp 문자열에 추가한다.
2. 만약 입력받은 문자열(data)과 temp 문자열이 같을 경우 해당 테스트 케이스 번호와 함께 1을 출력한다.
3. 만약 두 문자열이 다를 경우 해당 테스트 케이스 번호와 함께 0을 출력한다.

'''
