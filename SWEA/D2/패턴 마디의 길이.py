t = int(input())

for tc in range(1, t + 1) :
    data = input()
    result = 0

    for i in range(1, len(data)) :
        if data[i] == data[0] :
            if data[:i] == data[i:i*2] :
                result = i
                break
        if i == 29 :
            result = 30

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 문자열을 입력받아 1부터 문자열의 길이까지를 반복문의 범위로 지정한다.
2. 만약 현재 확인하고 있는 문자가 0번째 문자와 같다면 (3) 번을 수행한다.
3. 가장 첫 문자부터 i번째 문자까지의 문자열과 i번째 문자부터 i*2번째 문자까지의 문자열이 같다면 result에 i를 할당하고 break 한다.
4. 만약 i의 값이 29일 경우 result에 30을 할당한다.
5. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
