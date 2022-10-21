# https://www.acmicpc.net/problem/1202

import heapq

n, k = map(int, input().split())
data = []
for _ in range(n) :
    w, v = map(int, input().split()) # 무게, 가격
    heapq.heappush(data, (w, v))

bag = []
for _ in range(k) :
    able = int(input())
    heapq.heappush(bag, able)

result = 0
value = []
for _ in range(k) :
    pop = heapq.heappop(bag) # 최솟값 pop
    while data and data[0][0] <= pop : # 해당 보석이 pop 가방에 들어갈 수 있으면
        w, v = heapq.heappop(data)
        heapq.heappush(value, -v) # 가격 최대 힙으로

    if value :
        result += -heapq.heappop(value)
    elif not data :
        break

print(result)

'''
1. heapq 라이브러리를 통해 무게는 최소로 하되 훔칠 수 있는 보석의 최대 가격을 도출해내 해결한다.
 
2. n개의 보석의 정보를 입력받는데, 입력받은 무게(w)와 가격(v) 값을 data 리스트에 최소 힙으로 삽입한다.
 
3. k개의 가방 정보를 입력받는데, 입력받은 수용 무게(able) 값을 bag 리스트에 최소 힙으로 삽입한다.
 
4. 최소 힙으로 구성된 bag 리스트에서 요소를 하나씩 꺼내고(pop), 아직 보석이 남아있고 가장 먼저 확인하는 보석의 무게가 pop 이하일 경우 아래와 같은 작업을 반복 수행한다.
  - data 리스트에서 해당 보석의 무게와 가격을 꺼내 각 w, v에 할당한다.
  - 훔칠 수 있는 보석의 최대 가격을 구해야 하므로 가격(v) 값을 value 리스트에 최대 힙으로 삽입한다.
 
5. 만약 최대 힙으로 구성된 value에 값이 존재한다면 값을 하나 꺼내 result 값에 누적하고, 그렇지 않고 더 이상 보석이 없다면 break한다.

'''
