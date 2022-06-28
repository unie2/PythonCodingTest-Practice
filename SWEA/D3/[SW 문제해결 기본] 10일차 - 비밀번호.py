for tc in range(1, 11) :
    n, data = input().split()
    data = list(map(int, data))
    result = []
    for i in range(int(n)) :
        if result and result[-1] == data[i] :
            result.pop()
            continue
        result.append(data[i])

    print('#%d %d' % (tc, int(''.join(map(str, result)))))
    
'''
1. 각 테스트 케이스마다 입력받은 data를 리스트 형태로 구성하고, result 리스트를 초기화한다.
2. data 리스트의 요소를 하나씩 확인하며, 만약 result에 요소가 존재하고 result 리스트의 마지막 요소와 data[i]가 같을 경우 result의 마지막 요소를 제거하고 continue한다.
3. continue 되지 않았다면 result 리스트에 data[i]를 추가한다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 result 리스트의 요소를 이어 붙인 값을 출력한다.

'''
