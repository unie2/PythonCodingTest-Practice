n = int(input())

is_prime = [False, False] + [True] * (n - 1)
prime_list = []

for i in range(2, n + 1) :
    if is_prime[i] :
        prime_list.append(i)
        for j in range(i+i, n + 1, i) :
            is_prime[j] = False

result = 0
start = 0
end = 0

while end <= len(prime_list) :
    sum_value = sum(prime_list[start:end])
    if sum_value == n :
        result += 1
        end += 1
    elif sum_value < n :
        end += 1
    else :
        start += 1

print(result)

'''
1.가장 초기에 에라토스테네스의 체 알고리즘을 통해 소수로 이루어진 값들을 구해 prime_list에 저장한다.

2, end 값이 prime_list의 개수보다 커질 때까지 아래와 같은 작업을 반복 수행한다.
  - prime_list의 start 인덱스부터 end까지(end 미포함)의 합을 구하여 sum_value에 할당한다.
  - 만약 sum_value가 n이라면 result를 1증가시키고 end 값을 1 증가시킨다.
  - 만약 sum_value가 n보다 작을 경우 연속되는 수를 더 더해보아야 하므로 end 값을 1 증가시킨다.
  - 만약 sum_value가 n보다 클 경우 해당 방법으로 n을 만들지 못하였으므로 start를 1 증가시켜 다음 방법의 수를 확인한다.

'''
