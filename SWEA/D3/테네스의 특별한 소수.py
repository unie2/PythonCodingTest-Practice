t = int(input())
prime = [2]
visited = [0] * 1000001

for i in range(3, 1000001, 2) :
    if visited[i] == 0 : # 소수라면
        prime.append(i)
        for j in range(i, 1000001, i) :
            if j % i == 0 : # 소수가 아님
                visited[j] = 1

for tc in range(1, t + 1) :
    d, a, b = map(int, input().split())
    result = 0

    for p in prime :
        if a <= p <= b :
            if str(d) in str(p) :
                result += 1
        elif p > b :
            break

    print('#%d %d' % (tc, result))
    
'''
1. 3부터 시작하여 홀수 값을 확인하면서 해당 수가 visited 리스트에서 0 (소수)이라면 prime 리스트에 해당 값을 추가하고, 배수를 visited에서 1로 갱신한다.
2. 각 테스트 케이스마다 prime 리스트에서 소수를 하나씩 꺼내고, 만약 해당 값이 b보다 클경우 범위를 벗어나므로 더 이상 확인할 필요가 없으므로 break한다.
3. 만약 해당 수가 범위 내에 들어간다면 해당 수 중 d가 있는지 확인하고, 있다면 result 값을 1 증가시킨다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
