# https://www.acmicpc.net/problem/1697

from collections import deque

def bfs() :
    q = deque()
    q.append(n)

    while q :
        value = q.popleft()
        if value == k :
            print(data[value])
            break

        for next in (value + 1, value - 1, value * 2) :
            if 0 <= next <= 10 ** 5 and data[next] == 0 :
                data[next] = data[value] + 1
                q.append(next)

n, k = map(int, input().split())
data = [0] * (10 ** 5 + 1)

bfs()

'''
1. n, k의 값을 입력받고, 최댓값(100,001) 개수로 0으로 초기화한 data 리스트를 정의한 뒤 bfs() 함수를 호출한다.

2. bfs() 함수의 작업은 아래와 같다.
  - deque()를 통해 q를 정의하고 가장 초기에는 n의 값을 추가한다.
  - q가 빌때까지 반복 작업을 수행하는데, 작업은 아래와 같다.
    - q에서 값을 하나 꺼내고, 그 값(value)이 k와 같을 경우 가고자 하는 점에 도착했으므로 data[value]를 출력한 뒤 break한다.
    - (value+1, value-1, value*2)의 점에 대하여 각 점이 최대값 범위 안에 존재하고 data[next]의 값이 0일 경우
      원래의 점(data[value])에서 1을 더한 거리 값을 data[next]에 할당하고 q에 next를 추가한다.

'''
