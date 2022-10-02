# https://www.acmicpc.net/problem/1931

n = int(input())
time = [[0] * 2 for _ in range(n)]

for i in range(n) :
    start, end = map(int, input().split())
    time[i][0] = start
    time[i][1] = end

time.sort(key=lambda x: (x[1], x[0]))

result = 1
end_time = time[0][1]
for i in range(1, n) :
    if time[i][0] >= end_time :
        end_time = time[i][1]
        result += 1

print(result)


'''
1. 2차원 time 리스트를 정의하여 n개의 회의실의 시작시간과 끝나는 시간을 각각 time[i][0], time[i][1]에 할당한다.
 
2. 가장 많은 회의실을 이용할 수 있는 최대 횟수를 구하기 위해 회의가 빨리 끝나는 순으로 정렬한다.
 
3. 이후 정렬된 time 리스트에서 가장 첫 회의의 끝나는 시간을 end_time에 할당한 후 1번째 회의부터 확인한다.
 
4. time[i] 회의의 시작 시간이 end_time 값 이상이라면 회의가 겹치지 않으므로 end_time을 갱신하고 result 값을 1 증가시킨다.

'''
