# https://www.acmicpc.net/problem/1715

import heapq

n = int(input())
heap = []
for _ in range(n) :
    heapq.heappush(heap, int(input()))

if n == 1 :
    print(0)
else :
    total = 0
    while len(heap) > 1 :
        # 가장 작은 두개의 값 꺼내기
        pop_1 = heapq.heappop(heap)
        pop_2 = heapq.heappop(heap)
        # 비교 횟수 누적
        total += pop_1 + pop_2
        # heap에 다시 삽입
        heapq.heappush(heap, pop_1 + pop_2)

    print(total)
    
'''
1. heapq 라이브러리를 통해 heap 리스트에 있는 가장 작은 두개의 수를 꺼내 더하고, 이를 다시 리스트에 추가하는 방식으로 문제를 해결할 수 있다.
 
2. heappush()를 통해 n개의 수를 heap 리스트에 추가한다.
 
3. 만약 n이 1일 경우 비교할 필요가 없으므로 0을 출력하고, heap 리스트의 길이가 1보다 클 경우 아래의 작업을 반복 수행한다.
  - heap 리스트에서 가장 작은 두개의 값을 꺼내 각 pop_1, pop_2에 할당한다.
  - 두 수를 더해 total에 누적함으로써 비교 횟수를 누적한다.
  - 두 수를 더한 값을 다시 heap 리스트에 추가한다.

'''
