# https://www.acmicpc.net/problem/1655

# PyPy3 정답
import heapq

n = int(input())
leftheap = []
rightheap = []
result = []

for _ in range(n) :
    value = int(input())
    if len(leftheap) == len(rightheap) :
        heapq.heappush(leftheap, (-value, value))
    else :
        heapq.heappush(rightheap, (value, value))

    if rightheap and leftheap[0][1] > rightheap[0][0] :
        min_value = heapq.heappop(rightheap)[0]
        max_value = heapq.heappop(leftheap)[1]
        heapq.heappush(leftheap, (-min_value, min_value))
        heapq.heappush(rightheap, (max_value, max_value))

    result.append(leftheap[0][1])

for res in result :
    print(res)
    
    
'''
1. 중간 값을 기준으로 하여 더 작은 값들은 leftheap에, 더 큰 값들은 rightheap에 구성될 수 있도록 한다.
 
2. 값을 하나씩 입력받고, 만약 leftheap의 길이와 rightheap의 길이가 같을 경우 해당 값을 leftheap에 삽입한다.
 
3. 반면 두 길이가 다를 경우 길이를 맞춰주기 위해 해당 값을 rightheap에 삽입한다.
 
4. 만약 rightheap에 값이 있고 leftheap의 루트가 rightheap의 루트보다 크면 루트 값을 서로 바꿔준다.
 
5. 구성된 heap에서 중간 값(leftheap[0][1])을 도출해내 result 리스트에 추가하고, n개의 값에 대한 작업을 모두 마치면 최종적으로 result에 담겨 있는 요소들을 출력한다.

'''
