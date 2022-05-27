def solution(n) :
    answer = ''
    while n > 0 :
        a, b = divmod(n, 3)
        answer += str(b)
        n //= 3

    answer = int(answer, 3)

    return answer
  
'''
1. n이 0이 될 때까지 현재의 n을 3으로 나눈 나머지 값을 answer에 이어 붙인다.
2. 앞뒤가 반전된 3진법 answer을 다시 10진법으로 변환하여 반환한다.

'''
