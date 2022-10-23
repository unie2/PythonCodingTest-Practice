# https://www.acmicpc.net/problem/9576

t = int(input())
for _ in range(t) :
    n, m = map(int, input().split())
    flag = [False] * (n + 1)

    data = []
    for _ in range(m) :
        a, b = map(int, input().split())
        data.append((a, b))

    data.sort(key=lambda x: x[1])

    result = 0
    while data :
        a, b = data.pop(0)
        for i in range(a, b + 1) :
            if not flag[i] :
                flag[i] = True
                result += 1
                break

    print(result)
    
'''
1. 각 테스트케이스마다 n과 m을 입력받고, 각 책의 보유 여부를 담는 flag 리스트를 정의한다. (False면 책이 남아있음을 의미)
 
2. m개의 a, b를 입력받아 data 리스트에 추가하고, b 값을 기준으로 하여 오름차순으로 정렬한다.
 
3. data 리스트가 빌 때까지 아래와 같은 작업을 반복 수행한다.
  - data 리스트에서 우선순위가 가장 높은 요소를 꺼내 a, b에 할당한다.
  - a 이상 b 이하의 책 중에 아직 남아 있는 책이 있다면 해당 책의 flag 값을 True로 갱신하고 result를 1 증가시킨 후 break한다.

'''
