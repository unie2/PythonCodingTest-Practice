prime = []
for i in range(2, 1000) :
    for j in range(2, i // 2 + 1) :
        if i % j == 0 :
            break
    else :
        prime.append(i)

t = int(input())
for tc in range(1, t + 1) :
    n = int(input())
    result = 0

    for i in range(len(prime)) :
        if prime[i] < n :
            for j in range(i, len(prime)) :
                if prime[j] < n :
                    for k in range(j, len(prime)) :
                        if prime[i] + prime[j] + prime[k] == n :
                            result += 1

    print('#%d %d' % (tc, result))
    
'''
1. 2부터 999까지의 수 중 소수를 판별하여 prime 리스트에 저장한다.
2. 각 테스트 케이스마다 3중 for문을 통해 세 수를 도출하고, 세 수의 합이 n과 같다면 result 값을 1 증가시킨다.
3. 반복문이 모두 종료되면 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
