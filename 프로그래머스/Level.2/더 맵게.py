import heapq

def solution(scoville, K) :
    answer = 0
    target = []
    for value in scoville :
        heapq.heappush(target, value)

    while target[0] < K :
        try :
            heapq.heappush(target, heapq.heappop(target) + (heapq.heappop(target) * 2))
            answer += 1
        except :
            return -1

    return answer
  
'''
1. heapq를 통해 target에 scoville 리스트의 요소들을 삽입한다.

2. 가장 크기가 작은 원소가 K 이상이 될 때까지 반복 수행하며, 두 원소를 꺼내 아래와 같이 연산하여 target에 추가한다.
  - 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맴지 않은 음식의 스코빌 지수 * 2)

3. 위 연산 작업을 수행하면 answer 값을 1 증가시킨다.

4. 반복 수행이 종료되면 answer을 반환하고, 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없을 경우 -1을 반환한다.

'''
