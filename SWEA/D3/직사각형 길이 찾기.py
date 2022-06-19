t = int(input())

for tc in range(1, t + 1) :
    data = list(map(int, input().split()))
    result = 0
    if data.count(data[0]) == 3 :
        result = data[0]
    else :
        if data.count(max(data)) == 1 :
            result = max(data)
        else :
            result = min(data)

    print('#%d %d' % (tc, result))
    
    
'''
1. 각 테스트 케이스마다 3개의 값을 입력받아 data 리스트에 저장한다.
2. 만약 3개의 값이 모두 같다면 result에 해당 값을 할당한다.
3. 그렇지 않고, 만약 data 리스트에 존재하는 값 중 최댓값의 개수가 1일 경우 최댓값을 result에 할당한다.
4. 그렇지 않다면 최솟값을 result에 할당한다.
5. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
