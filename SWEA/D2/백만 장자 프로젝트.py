t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    info = list(map(int, input().split()))

    max_value = info[-1]
    result = 0

    for i in range(n-2, -1, -1) :
        if info[i] >= max_value :
            max_value = info[i]
        else :
            result += max_value - info[i]

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 n개의 자연수를 입력받아 info 리스트를 정의한다.
2. info 리스트의 마지막 요소 값을 최댓값으로 임시로 정해 max_value 에 할당한다.
3. 반복문을 통해 info 리스트 요소를 거꾸로 확인하는데, 만약 해당 값이 max_value 보다 크거나 같을 경우 max_value를 해당 값(info[i])으로 갱신한다.
4. 해당 값이 max_value 보다 작다면 max_value에서 해당 값을 뺀 값을 result 에 누적한다.
5. 반복문이 종료되면 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
