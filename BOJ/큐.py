import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n) :
    order = list(input().split())
    if len(order) == 2 : # 'push X'일 경우
        data.append(int(order[1]))
    elif order[0] == 'pop' :
        if len(data) == 0 :
            print(-1)
        else :
            pop_value = data.pop(0)
            print(pop_value)
    elif order[0] == 'size' :
        print(len(data))
    elif order[0] == 'empty' :
        if len(data) == 0 :
            print(1)
        else :
            print(0)
    elif order[0] == 'front' :
        if len(data) == 0 :
            print(-1)
        else :
            print(data[0])
    elif order[0] == 'back' :
        if len(data) == 0 :
            print(-1)
        else :
            print(data[-1])
            
'''
1. sys.stdin.readline 을 input에 할당하여 값을 입력받을 때 사용하도록 한다.

2. 각 입력마다 order 리스트에 저장하는데, 만약 order 리스트의 요소 개수가 2일 경우 'push X'에 해당되므로 아래와 같은 작업을 수행한다.
  - order[1] 값을 정수형으로 변환하여 data 리스트에 추가한다.

3. 만약 order[0] 값이 'pop'일 경우 아래와 같은 작업을 수행한다.
  - 만약 data의 길이가 0일 경우 큐에 들어있는 정수가 없음을 의미하기 때문에 -1을 출력한다.
  - 큐에 정수가 있을 경우 첫 번째 값을 빼내어 pop_value에 할당한 후 출력한다.

4. 만약 order[0] 값이 'size'일 경우 data의 길이를 출력한다.

5. 만약 order[0] 값이 'empty'일 경우 아래와 같은 작업을 수행한다.
  - data의 길이가 0일 경우 1을 출력하고, 0이 아닐 경우 0을 출력한다.

6. 만약 order[0] 값이 'front'일 경우 아래와 같은 작업을 수행한다.
  - data의 길이가 0일 경우 -1을 출력하고, 그렇지 않다면 data의 가장 첫 번째 요소를 출력한다.

7. 만약 order[0] 값이 'back'일 경우 아래와 같은 작업을 수행한다.
  - data의 길이가 0인 경우 -1을 출력하고, 그렇지 않다면 data의 가장 마지막 요소를 출력한다.

'''
