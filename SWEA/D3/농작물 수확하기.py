t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    start, end = n // 2, n // 2

    result = 0
    for i in range(n) :
        for j in range(start, end + 1) :
            result += data[i][j]

        if i < n // 2 :
            start -= 1
            end += 1
        else :
            start += 1
            end -= 1

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력받은 n을 2로 나눈 값을 start와 end에 할당한다.
2. 2중 for문을 통해 data[i][j] 값을 result에 누적한다.
3. 한 열에 대한 반복 작업이 끝나고, 만약 현재의 i가 중간 값보다 작을 경우 start를 1 감소시키고 end를 1 증가시킨다.
4. 그렇지 않다면 반대로 start를 1 증가시키고 end를 1 감소시킨다.
5. 반복 수행이 모두 끝나면 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
