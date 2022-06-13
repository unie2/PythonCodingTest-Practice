t = int(input())

for tc in range(1, t + 1) :
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    result = []

    for i in range(1, n + 1) :
        if i not in data :
            result.append(i)

    print(f'#{tc}', *result)
    
'''
1. 각 테스트 케이스마다 입력받은 k개의 수를 data 리스트에 저장한다.
2. 1부터 n + 1까지를 반복문의 범위로 설정하여 i가 data 리스트에 존재하지 않는다면 result 리스트에 i를 추가한다.
3. 최종적으로 해당 테스트 케이스 번호와 함께 result 리스트의 요소를 출력한다.

'''
