def is_prime(value) :
    if value > max_value :
        for prime in primes :
            if prime >= value :
                break
            elif value % prime == 0 :
                return False

        return True
    else :
        return data[value]

max_value = 2000000
data = [False, False] + [True for _ in range(max_value-1)]
primes = []
for i in range(2, max_value + 1) :
    if data[i] :
        primes.append(i)
        for j in range(i+i, max_value, i) :
            data[j] = False

t = int(input())
for _ in range(t) :
    a, b = map(int, input().split())
    sum_value = a + b

    if sum_value < 4 :
        print('NO')
    elif sum_value % 2 == 0 :
        print('YES')
    else :
        if is_prime(sum_value - 2) :
            print('YES')
        else :
            print('NO')
            
'''
1. 에라토스테네스의 체 알고리즘을 통해 2,000,000까지의 수 중 소수인 수를 primes 리스트에 저장한다.

2. a와 b의 합을 sum_value에 저장하고, 그 값이 4보다 작다면 소수로 나눌 수 없으므로 'NO'를 출력한다.

3. 그렇지 않고, 값이 4 이상이고 짝수일 경우 무조건 소수로 나눌 수 있으므로 'YES'를 출력한다. (골드바흐의 추측)

4. 이 외 홀수 소수는 2와 홀수 소수의 조합으로만 가능하므로 is_prime() 함수를 통해 sum_value - 2 값이 소수인지 판별하고, 소수라면 'YES'를, 아니라면 'NO'를 출력한다.

5. 특정 값이 소수인지 판별하는 is_prime() 함수의 작업은 아래와 같다.
  - 만약 값이 최대 값(max_value)보다 큰 경우 해당 수가 소수로 나누어 떨어지는지 확인하고, 나누어 떨어진다면 소수가 아니므로 False를, 나누어 떨어지는 수가 없으면 True를 반환한다.
  - 값이 최대 값 이하인 경우 정의했던 소수 여부 리스트(data)에서 해당 값이 소수인지 아닌지에 대한 여부를 반환한다.

'''
