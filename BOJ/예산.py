# https://www.acmicpc.net/problem/2512

n = int(input())
data = list(map(int, input().split()))
m = int(input())
start, end = 0, max(data)

while start <= end :
    mid = (start + end) // 2
    count = 0
    for d in data :
        if d > mid :
            count += mid
        else :
            count += d

    if count <= m :
        start = mid + 1
    else :
        end = mid - 1

print(end)

'''
1. 이분 탐색을 통해 배정된 예산들 중 최댓값인 정수를 구해 출력한다.
 
2. start와 end 값을 각 0과 data 리스트 중 최댓값으로 초기화한 후 start가 end보다 커질 때까지 아래와 같은 작업을 반복한다.
  - start와 end의 중간 값을 구해 mid에 할당하고, 배정된 예산들의 총합을 담을 count 변수를 0으로 초기화한다.
  - data 리스트의 요소들을 하나씩 꺼내는데, 해당 요소가 mid 값보다 클 경우 상한액 이상이므로 mid를 count에 누적한다.
  - 반대로 해당 요소가 mid 이하일 경우 그 값을 count에 누적한다.
  
  - 만약 모두 누적한 총합(count)이 m 이하일 경우 mid를 더 높게 잡을 수 있으므로 mid+1을 start에 갱신한다.
  - 반대로 count가 m보다 클 경우 더 낮게 잡아야하므로 mid-1을 end에 갱신한다.

'''
