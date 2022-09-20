n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    data[i][0] = min(data[i-1][1], data[i-1][2]) + data[i][0]
    data[i][1] = min(data[i-1][0], data[i-1][2]) + data[i][1]
    data[i][2] = min(data[i-1][0], data[i-1][1]) + data[i][2]

print(min(data[n-1][0], data[n-1][1], data[n-1][2]))

'''
1. 다이나믹 프로그래밍을 통해 문제를 해결할 수 있다.
2. 1부터 n까지를 반복문의 범위로 설정하여 각 data[i][x]에 이전 좌표에서 가능한 인덱스의 최소값과 현재 좌표의 최소값을 더하여 갱신한다.
3. 최종적으로 마지막 인덱스의 0번째, 1번째, 2번째 값 중 최솟값을 출력한다.

'''
