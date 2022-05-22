from collections import deque

def solution(prices) :
    answer = []
    prices = deque(prices)
    while prices :
        cnt = 0
        price = prices.popleft()

        for i in prices :
            cnt += 1
            if price > i :
                break

        answer.append(cnt)

    return answer
  
'''
1. 전달받은 prices 리스트를 deque로 감싸 갱신한다.

2. prices가 빌 때까지 아래와 같은 작업을 반복 수행한다.
  - prices의 가장 앞에 있는 요소를 빼어 price에 할당한다.
  - 남아 있는 prices의 요소들을 확인하며, cnt를 1 증가시키고 price가 확인하는 요소보다 클 경우 break 한다.
  - for문을 빠져나오면 answer에 cnt를 추가하고, 이와 같은 작업이 담겨 있는 while문이 끝나면 최종적으로 answer을 반환한다.

'''
