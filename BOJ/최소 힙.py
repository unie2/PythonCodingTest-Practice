# https://www.acmicpc.net/problem/1927

import heapq

n = int(input())
data = []

result = []
for _ in range(n) :
    x = int(input())
    if x == 0 :
        if not data :
            result.append(0)
        else :
            result.append(heapq.heappop(data))
    else :
        heapq.heappush(data, x)

for res in result :
    print(res)
    
    
'''
1. heapq 라이브러리를 통해 문제를 해결할 수 있다.
 
2. n개의 수를 입력받는데, 각 수가 0일 경우 아래 조건 중 해당하는 조건에 맞도록 작업을 수행한다.
  - 만약 data 리스트에 값이 존재하지 않는다면 result 리스트에 0을 추가한다.
  - 그렇지 않다면 data 리스트에서 가장 작은 값을 꺼내 result 리스트에 추가한다.
 
3. 해당 수가 0이 아닐 경우 heappush()를 통해 data 리스트에 입력 값을 추가한다.
 
4. result 리스트에 존재하는 값들을 차례대로 하나씩 출력한다.

'''
