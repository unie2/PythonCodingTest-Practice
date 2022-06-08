t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = [0] * 5001
    for _ in range(n) :
        a, b = map(int, input().split())
        for i in range(a, b + 1) :
            data[i] += 1

    result = []
    p = int(input())
    for _ in range(p) :
        c = int(input())
        result.append(data[c])

    print(f'#{tc}', *result)
    
'''
1. 각 테스트 케이스마다 0으로 초기화 시킨 5001개의 데이터를 갖는 data 리스트를 정의한다.
2. 입력받은 a를 반복문의 시작값으로, b+1을 끝값으로 설정하여 data[i] 의 값을 1씩 증가시킨다.
3. 증가 작업이 끝나면 p개의 수를 입력받고, 각 수에 대하여 data[c] 값을 result 리스트에 추가한다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 result 리스트의 요소들을 출력한다.

'''
