def solution(n) :
    answer = ''
    while n > 0 :
        if n % 3 == 0 :
            answer += str(4)
            n = n // 3 - 1
        else :
            answer += str(n % 3)
            n = n // 3

    return answer[::-1]
  
'''
1. 3진법을 사용하며, n이 0 이하가 될 때까지 while문을 통해 반복 작업을 수행한다. 작업은 아래와 같다.
  - 만약 현재의 n 값이 3의 배수일 경우 answer에 4를 이어붙이고 n을 3으로 나눈 몫에서 1을 뺀 값으로 갱신한다.
  - 현재의 n 값이 3의 배수가 아닐 경우 n을 3으로 나눈 나머지 값을 answer에 이어 붙이고 n을 3으로 나눈 몫으로 갱신한다.

2. 반복 작업이 끝나면 문자열 answer을 역순으로 하여 반환한다.

'''
