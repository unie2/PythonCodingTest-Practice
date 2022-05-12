t = int(input())

for tc in range(1, t + 1) :
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(n-m+1) :
        for j in range(n-m+1) :
            sum_value = 0
            for k in range(m) :
                for l in range(m) :
                    sum_value += board[i+k][j+l]
            if sum_value > result :
                result = sum_value

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 N x N 크기의 배열을 입력받는다.
2. n-m+1 의 값을 반복문의 범위로 지정하여 M x M 크기의 파리채를 한 칸씩 옮겨 죽인 파리의 개수를 sum_value에 누적한다.
3. 만약 sum_value의 값이 result 값보다 클 경우 result 값을 sum_value 값으로 갱신한다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
