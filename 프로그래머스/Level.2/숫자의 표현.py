def solution(n) :
    answer = 0

    for i in range(1, n // 2 + 1) :
        sum_value = 0
        for j in range(i, n + 1) :
            sum_value += j
            if sum_value == n :
                answer += 1
                break
            elif sum_value > n :
                break

    return answer + 1
  
'''
1. 이중 for문을 통해 연속한 자연수의 합을 구하며, 첫번째 반복문의 범위는 n의 반으로 설정하고, 두 번째 반복문의 범위는 i부터 n까지로 설정한다.
2. sum_value에 j를 더하고, sum_value가 n일 경우 answer을 1 증가시킨 후 break한다.
3. 만약 sum_value가 n보다 커진다면 break한다.
4. 최종적으로 answer 값을 반환할 때는 자기 자신을 포함해야하므로 1을 더하여 반환한다.

'''
