from collections import deque

t = int(input())

for _ in range(t) :
    p = input()
    n = int(input())
    data = input()[1:-1].split(',')
    q = deque(data)

    if n == 0 :
        q = []

    reverse = 0
    flag = 0
    for value in p :
        if value == 'R' :
            reverse += 1
        elif value == 'D' :
            if q :
                if reverse % 2 == 0 : # 그대로
                    q.popleft()
                else : # 거꾸로
                    q.pop()
            else :
                flag = 1
                print('error')
                break

    if flag == 0 :
        if reverse % 2 == 0 : # 그대로
            print('[' + ','.join(q) + ']')
        else : # 거꾸로
            q.reverse()
            print('[' + ','.join(q) + ']')
            
'''
1. 입력받은 배열의 괄호([, ])를 제외하여 ',' 로 구분하여 data에 저장한 후, deque()로 감싸 q에 저장한다.
2. 만약 n이 0일 경우 q를 '[]'로 갱신한다.
3. 입력받은 p의 값을 하나씩 확인하는데, 만약 그 값이 'R'일 경우 reverse를 1 증가시킨다.
4. 그 값이 'D'이고 q에 값이 존재하며, reverse 값이 짝수일 경우 입력받은 그대로 수행하면 되므로 popleft()를 통해 앞 요소를 제거한다.
5. 값이 'D'이고 q에 값이 존재하지 않는다면 flag를 1로 갱신하고 'error'를 출력한 후 break 한다.
6. p의 모든 값을 확인한 후 flag 값이 0이고 reverse가 짝수라면 join()을 활용하여 값을 그대로 출력한다.
7. reverse가 홀수라면 reverse()를 통해 값을 뒤집고, join()을 활용하여 값을 출력한다.

'''
