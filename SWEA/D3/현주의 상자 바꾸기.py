t = int(input())

for tc in range(1, t + 1) :
    n, q = map(int, input().split())
    data = [0] * n
    for i in range(1, q + 1) :
        l, r = map(int, input().split())
        for j in range(l-1, r) :
            data[j] = i

    print(f'#{tc}', *data)
    
'''
1. 각 테스트 케이스마다 0으로 초기화 된 n개의 데이터를 담은 data 리스트를 정의한다.
2. 1부터 q + 1까지를 반복문의 범위로 설정하고, l, r을 입력받은 후 data 리스트의 l 이상 r 이하의 인덱스 값을 i로 갱신한다.
3. 반복문이 종료되면 최종적으로 해당 테스트 케이스 번호와 함께 data 리스트의 요소를 출력한다.

'''
