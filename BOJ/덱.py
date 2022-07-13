from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque([])
for _ in range(n) :
    order = list(input().split())
    if order[0] == 'push_front' : # 정수 X를 덱의 앞에 넣는다.
        q.insert(0, int(order[1]))
    elif order[0] == 'push_back' : # 정수 X를 덱의 뒤에 넣는다.
        q.append(int(order[1]))
    elif order[0] == 'pop_front' : # 덱의 가장 앞 수 빼고 출력
        if len(q) == 0 :
            print(-1)
        else :
            print(q.popleft())
    elif order[0] == 'pop_back' : # 덱의 가장 뒷 수 빼고 출력
        if len(q) == 0 :
            print(-1)
        else :
            print(q.pop())
    elif order[0] == 'size' : # 덱에 들어있는 정수의 개수 출력
        print(len(q))
    elif order[0] == 'empty' : # 비어있으면 1, 아니면 0 출력
        if len(q) == 0 :
            print(1)
        else :
            print(0)
    elif order[0] == 'front' : # 가장 앞 수 출력
        if len(q) == 0 :
            print(-1)
        else :
            print(q[0])
    elif order[0] == 'back' : # 가장 뒷 수 출력
        if len(q) == 0 :
            print(-1)
        else :
            print(q[-1])
            
'''
1. sys.stdin.readline 을 input에 할당하여 값을 입력받을 때 사용하도록 한다.

2. 각 입력마다 order 리스트에 저장하는데, 만약 order[0] 값이 'push_front' 일 경우 q의 가장 첫 번째 요소에 정수형 order[1]을 추가한다.

3. order[0] 값이 'push_back'일 경우 q의 가장 마지막 요소에 정수형 order[1]을 추가한다.

4. order[0] 값이 'pop_front'일 경우 아래와 같은 작업을 수행한다.
  - 만약 q의 길이가 0일 경우 -1을 출력하고, 그렇지 않다면 q의 가장 앞에 존재하는 수를 빼내어 출력한다.

5. order[0] 값이 'pop_back'일 경우 아래와 같은 작업을 수행한다.
  - 만약 q의 길이가 0일 경우 -1을 출력하고, 그렇지 않다면 q의 가장 마지막 인덱스에 존재하는 수를 빼내어 출력한다.

6. order[0] 값이 'size'일 경우 q에 들어있는 정수의 개수를 출력한다.

7. order[0] 값이 'empty'일 경우 q의 길이를 확인하고, 그 값이 0이라면 1을, 아니라면 0을 출력한다.

8. order[0] 값이 'front'일 경우 아래와 같은 작업을 수행한다.
  - q의 길이가 0일 경우 -1을 출력하고, 그렇지 않다면 q의 가장 첫 번째 요소를 출력한다.

9. order[0] 값이 'back'일 경우 아래와 같은 작업을 수행한다.
  - q의 길이가 0일 경우 -1을 출력하고, 그렇지 않다면 q의 가장 마지막 요소를 출력한다.

'''
