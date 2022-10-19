# https://www.acmicpc.net/problem/1826

import heapq

n = int(input())
temp = []
for _ in range(n) :
    heapq.heappush(temp, list(map(int, input().split())))

l, p = map(int, input().split())
result = 0
heap = []

# 현재의 연료로 마을까지 갈 수 있어야 한다.
while p < l :
    # 다음 주유소가 있고, 현재의 연료로 다음 주유소에 갈 수 있는지 확인
    while temp and temp[0][0] <= p :
        a, b = heapq.heappop(temp) # 성경이의 시작위치에서 주유소까지의 거리, 그 주유소에서 채울 수 있는 연료의 양
        heapq.heappush(heap, [-b, a]) # 많이 채울 수 있는 연료의 양 순으로

    if not heap :
        result = -1
        break

    b, a = heapq.heappop(heap)
    # 연료 채우기
    p += -b # heap에 -b로 담겨져 있으므로
    result += 1

print(result)


'''
1. heapq를 통해 n개의 주유소 정보를 temp 리스트에 할당한다.
 
2. 현재의 연료(p)로 마을까지 갈 수 있어야 하므로, p가 성경이의 위치에서 마을까지의 거리(l)보다 작은 값일 동안에 아래와 같은 작업을 반복한다.
  - temp에 요소가 존재하고 가장 먼저 도출되는 값의 마을까지의 거리가 현재의 연료로 갈 수 있다면 heap 리스트에 [-b, a] 형태로 값을 삽입한다. 
    즉, 채울 수 있는 연료의 양의 경우 최대 힙으로 삽입될 수 있도록 한다.
 
  - 만약 heap 리스트에 요소가 없다면 마을에 도착하지 못하는 경우이므로 result에 -1을 할당하고 break한다.
  - heap 리스트에 요소가 존재할 경우 우선순위가 높은 값을 꺼내 각 b, a에 할당하고, p에 -b를 누적함으로써 연료를 채운 후 result 값을 1 증가시킨다.

'''
