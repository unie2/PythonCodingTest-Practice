def solution(N, number) :
    answer = -1
    dp = [[] for _ in range(9)]
    for i in range(1, 9) :
        dp[i].append(int(str(N) * i))
        for j in range(1, i) :
            for num1 in dp[j] :
                for num2 in dp[i-j] :
                    dp[i].append(num1 + num2)
                    dp[i].append(num1 - num2)
                    dp[i].append(num1 * num2)
                    if num2 != 0 :
                        dp[i].append(num1 // num2)

        dp[i] = list(set(dp[i]))
        if number in dp[i] :
            return i

    return answer
  
'''
1. 이전 값을 활용하기 위해 사칙연산을 수행한 값들을 저장할 수 있는 dp 리스트를 정의한다.
2. str(N) * i 의 값을 정수형으로 변환하여 dp[i]에 추가하고 이전에 저장된 값들을 활용하여 사칙연산을 수행한다.
3. 만약 dp[i]에 number가 존재할 경우 i를 반환하고, 반복문이 모두 끝났음에도 반환되지 않았다면 -1을 반환한다.

'''
