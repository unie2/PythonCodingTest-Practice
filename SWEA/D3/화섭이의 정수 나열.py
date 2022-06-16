t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    value = ''
    while True :
        value += ''.join(map(str, input().split()))
        if len(value) == n :
            break

    result = 0
    cnt = 0
    while True :
        if str(cnt) not in value :
            result = cnt
            break
        cnt += 1

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 n개의 정수를 입력받아 문자열 형태로 변환하여 value에 저장한다.
2. cnt를 0부터 시작하여 1씩 증가시키면서 while문을 통해 value에 존재하는지 확인한다.
3. 만약 cnt를 문자형으로 변환한 값이 value 문자열에 존재하지 않는다면 result에 cnt를 삽입하고 break한다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
