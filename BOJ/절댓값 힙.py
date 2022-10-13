# https://www.acmicpc.net/problem/11286

# PyPy3 정답
import heapq

n = int(input())
heap = []

result = []
for _ in range(n) :
    x = int(input())
    if x == 0 :
        try :
            result.append(heapq.heappop(heap)[1])
        except :
            result.append(0)
    else :
        heapq.heappush(heap, (abs(x), x))

for res in result :
    print(res)
    
'''
1. heapq 라이브러리를 통해 문제를 해결할 수 있다.
 
2. n개의 수를 입력받는데, 각 수가 0일 경우 아래 조건 중 해당하는 조건에 맞도록 작업을 수행한다.
  - 만약 heap 리스트에 값이 존재한다면 result 리스트에 절댓값이 가장 작은 값을 출력한다.
    이때 절댓값이 가장 작은 값이 여러 개일 경우에는 가장 작은 수를 대상으로 한다.
  - 그렇지 않다면 result 리스트에 0을 추가한다.
 
3. 해당 수가 0이 아닐 경우 heappush()를 통해 heap 리스트에 (입력 값의 절댓값, 입력 값)을 추가한다.
 
4. result 리스트에 존재하는 값들을 차례대로 하나씩 출력한다.

'''
