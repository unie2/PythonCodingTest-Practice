import sys
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n) :
    order = list(input().split())
    if len(order) == 2 : # push X 일경우
        insert_value = int(order[1])
        q.append(insert_value)
        continue
    if order[0] == 'pop' :
        if len(q) == 0 : # 스택에 들어있는 정수가 없는 경우
            print(-1)
        else :
            pop_value = q.pop()
            print(pop_value)
    elif order[0] == 'size' :
        print(len(q))
    elif order[0] == 'empty' :
        if len(q) == 0 :
            print(1)
        else :
            print(0)
    elif order[0] == 'top' :
        if len(q) == 0 :
            print(-1)
        else :
            value = q[-1]
            print(value)
            
'''
1. sys.stdin.readline 을 input에 할당하여 값을 입력받을 때 사용하도록 한다.

2. 각 입력마다 order 리스트에 저장하는데, 만약 order 리스트의 요소 개수가 2일 경우 'push X'에 해당되므로 아래와 같은 작업을 수행한다.
  - order[1] 값을 정수형으로 변환하여 insert_value에 할당한다.
  - q 리스트에 insert_value 값을 추가한 후 continue를 수행한다.

3. 만약 order[0] 값이 'pop'일 경우 아래와 같은 작업을 수행한다.
  - 만약 q의 길이가 0일 경우 스택에 들어있는 정수가 없음을 의미하기 때문에 -1을 출력한다.
  - 스택에 정수가 있을 경우 가장 마지막에 할당한 값을 빼내어 pop_value에 할당한 후 출력한다.

4. 만약 order[0] 값이 'size'일 경우 q의 길이를 출력한다.

5. 만약 order[0] 값이 'empty'일 경우 아래와 같은 작업을 수행한다.
  - q의 길이가 0일 경우 1을 출력하고, 0이 아닐 경우 0을 출력한다.

6. 만약 order[0] 값이 'top'일 경우 아래와 같은 작업을 수행한다.
  - q의 길이가 0일 경우 -1을 출력하고, 그렇지 않다면 q의 가장 마지막 요소를 출력한다.

'''
